import logging

from comments.crawlers import crawl_new_post_comments
from fbCrawler.celery import app

logger = logging.getLogger(__name__)


@app.task
def crawl_post_comments(pid, post_id):
    crawl_new_post_comments(pid, post_id)
    logger.info(f'Crawl process for post comments of {pid}_{post_id} is done')
