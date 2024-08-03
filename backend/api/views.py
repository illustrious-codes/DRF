from urllib import request
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    print(body)
    return JsonResponse({"David": "Hi dear, this is your first api response"})