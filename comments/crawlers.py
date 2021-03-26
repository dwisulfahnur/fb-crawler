import logging
import sys
import time
import traceback
import urllib.parse as urlparse
from urllib.parse import parse_qs

from bs4 import BeautifulSoup
from django.conf import settings
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from comments.helpers import save_post_comment

logger = logging.getLogger(__name__)


def get_selenium_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    if settings.SELENIUM_REMOTE_EXECUTOR:
        driver = webdriver.Remote(
            command_executor=settings.SELENIUM_REMOTE_EXECUTOR,
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options,
        )
        return driver
    else:
        driver = webdriver.Chrome(
            executable_path="/usr/local/bin/chromedriver",
            chrome_options=options
        )
        return driver


def crawl_new_post_comments(pid, post_id):
    save_post_comment(pid, post_id)
    try:
        comments = get_post_comments(pid, post_id)
        save_post_comment(pid=pid, post_id=post_id, data=comments)
        logger.info(f'Crawl process for post comments of {pid}_{post_id} is done, ({len(comments)}) collected')
        return comments
    except:
        out = save_post_comment(pid, post_id, failed=True)
        logger.error(traceback.print_exception(*sys.exc_info()))
        logger.error(f'Crawl process for post comments of {pid}_{post_id} is Failed')
        return out


def get_qs_of_url(url):
    parsed = urlparse.urlparse(url)
    return parse_qs(parsed.query)


def get_post_html(pid, post_id):
    browser = get_selenium_driver()

    url = f'https://www.facebook.com/story.php?story_fbid={post_id}&id={pid}'
    browser.get(url)

    time.sleep(5)
    skip = browser.find_element_by_id('expanding_cta_close_button')
    browser.execute_script('arguments[0].click();', skip)

    # Load Comments
    comment_buttons = browser.find_elements_by_css_selector(
        "div.userContentWrapper a[role=button][data-ft='{\"tn\":\"O\"}']")

    for button in comment_buttons:
        logger.info('Load Comments...')
        browser.execute_script('arguments[0].click();', button)
        time.sleep(2)

    show_dropdown_button = browser.find_element_by_css_selector(
        'div.userContentWrapper a[data-ordering=RANKED_THREADED]')
    browser.execute_script('arguments[0].click();', show_dropdown_button)
    time.sleep(0.5)

    dropdowns = browser.find_elements_by_xpath("//div//ul[@role = 'menu']//li[@role = 'presentation']//a")
    browser.execute_script('arguments[0].click();', dropdowns[-1])
    time.sleep(2)

    def get_show_reply_buttons(driver):
        return driver.find_elements_by_css_selector(
            "div.userContentWrapper a[role=button][data-ft='{\"tn\":\"Q\"}']")

    def load_reply_buttons(driver):
        buttons = get_show_reply_buttons(driver)
        for btn in buttons:
            driver.execute_script('arguments[0].click();', btn)
            logger.info('Load More Comments...')
            time.sleep(0.2)
        time.sleep(1)
        last_replies = get_show_reply_buttons(driver)
        if len(last_replies) > 0:
            load_reply_buttons(driver)

    load_reply_buttons(browser)
    html = browser.page_source
    browser.quit()
    return html


def get_post_comments(pid, post_id):
    html = get_post_html(pid, post_id)
    soup = BeautifulSoup(html, 'lxml')

    comments = soup.select('.userContentWrapper h6 ~ ul > li')
    data = []
    for comment in comments:
        comment, replies = tuple(comment.children)
        comment = comment.select('div > ul > li div[role=article]')[0]
        replies = replies.select('div > ul > li div[role=article]')

        user_comment = comment.select('a')[0]['href']
        if '/profile.php' in user_comment:
            user_comment = get_qs_of_url(user_comment).get('id')
        else:
            user_comment = user_comment.split('?')[0].replace('/', '')
        id_comment = get_qs_of_url(comment.select('ul:only-child > li > span + a')[0]['href']).get('comment_id')[0]
        text_comment = comment.select('a ~ span > span, span ~ span > span')
        text_comment = text_comment[0].text if text_comment else ''
        date_comment = comment.select('ul:only-child li abbr')[0]['data-utime']

        data.append({
            'id_post': pid,
            'parent_id_comment': None,
            'id_comment': id_comment,
            'user_comment': user_comment,
            'text_comment': text_comment,
            'date_comment': date_comment,
            'count_replies': len(replies),
        })

        for reply in replies:
            user_reply = reply.select('a')[0]['href']
            if '/profile.php' in user_reply:
                user_reply = get_qs_of_url(user_reply).get('id')
            else:
                user_reply = user_reply.split('?')[0].replace('/', '')
            id_reply = get_qs_of_url(
                reply.select('ul:only-child > li > span + a')[0]['href']
            ).get('reply_comment_id')[0]
            text_reply = reply.select('a ~ span > span, span ~ span > span')
            text_reply = getattr(text_reply[0], 'text', '') if text_reply else ''
            date_reply = reply.select('ul:only-child li abbr')[0]['data-utime']
            data.append({
                'id_post': pid,
                'parent_id_comment': id_comment,
                'id_comment': id_reply,
                'user_comment': user_reply,
                'text_comment': text_reply,
                'date_comment': date_reply,
                'count_replies': None,
            })

    return data
