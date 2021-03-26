import os
import pathlib

import ujson
from django.conf import settings


def get_output_dirs():
    """
    Get directory output for comment
    :return:
    """
    directory = os.path.join(settings.BASE_DIR, 'media', 'post_comments')
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
    return directory


def save_post_comment(pid, post_id, data=None, failed=False):
    filename = f'{post_id}.json'
    target_dir = os.path.join(get_output_dirs(), filename)
    status = 'on_progress'
    if data:
        status = 'completed'
    if failed:
        status = 'failed'

    data_out = {
        'pid': pid,
        'post_id': post_id,
        'status': status,
        'comments': data
    }

    if not os.path.isfile(target_dir):
        with open(target_dir, 'w') as outfile:
            ujson.dump(data_out, outfile)
        outfile.close()

    with open(target_dir, 'w') as outfile:
        outfile.truncate(0)
        ujson.dump(data_out, outfile)
        outfile.close()

    return data_out


def get_post_comments_data(post_id):
    comment_post_dir = get_output_dirs()
    filedir = os.path.join(comment_post_dir, f'{post_id}.json')
    if os.path.isfile(filedir):
        with open(filedir) as f:
            data = ujson.load(f)
            f.close()
            return data
    return {}
