from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from comments.helpers import get_post_comments_data, save_post_comment
from comments.tasks import crawl_post_comments


@csrf_exempt
@require_http_methods(["POST"])
def crawl_post_comments_api(request, pid, post_id):
    data = get_post_comments_data(post_id)

    # Only crawl data if it doesnt exists yet or failure
    if not data or data.get('status') not in ['on_progress', 'completed']:
        crawl_post_comments.delay(pid, post_id)

    if not data.get('status'):
        data = save_post_comment(pid, post_id)
    return JsonResponse(
        data=data,
        status=200
    )


@require_http_methods(["GET"])
def get_post_commments_api(request, post_id):
    data = get_post_comments_data(post_id)
    if not data:
        return JsonResponse(
            status=404,
            data={
                'success': False,
                'code': 404
            })
    return JsonResponse(data=data, status=200)
