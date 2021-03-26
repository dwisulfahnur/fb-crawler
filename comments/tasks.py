import logging


from fbCrawler.celery import app

logger = logging.getLogger(__name__)


@app.task
def crawl_post_comments(pid, post_id):
    from comments.crawlers import crawl_new_post_comments
    crawl_new_post_comments(pid, post_id)
    return "done"
