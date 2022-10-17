from ninja import NinjaAPI
from ninja.renderers import BaseRenderer
import json
import requests, random, re
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from chatbot.settings import (
    VERIFY_TOKEN,
    PAGE_ACCESS_TOKEN,
)


# !!! The following code uses Django Ninja which is not currently supporting multiple
# http requests (GET, POST) to same endpoint. Need to use django generic view instead.
# Keeping code so that I can implement when support is added to django Ninja
# issue ref: https://github.com/vitalik/django-ninja/issues/590
#
# class WebhookResponse(BaseRenderer):
#     media_type = "text/plain"
#
#     def render(self, request, data, *, response_status):
#         return data
#
# # scope out additional api Module in order to customize response as plain text
# api_plain_text = NinjaAPI(renderer=WebhookResponse(), urls_namespace='webhooks')
#
# # GET support for webhook
# # using fb_api namespace to return challenge as plain text
# @api_plain_text.get("/webhooks/webhook", response={403: str, 400: str, 200: str})
# def init_messenger(request):
#     verify_token = request.GET.get('hub.verify_token')
#     mode = request.GET.get('hub.mode')
#     challenge = request.GET.get('hub.challenge')
#
#     if mode and verify_token and challenge:
#         if mode == 'subscribe' and verify_token == VERIFY_TOKEN:
#             return challenge
#         else:
#             return 403, ""
#     return 400, ""
#
# router = Router()
#
#
# class SuccessResponse(Schema):
#     message: str
#
# class Error(Schema):
#     message: str
#
# class ActualMessage(Schema):
#     message: str
#
# class Messages(Schema):
#     messaging: List[ActualMessage]
#
# class MessengerBody(Schema):
#     object: str
#     entry: List[Messages]
#
#
# use following when http issue resolved with django ninja
# @router.post("/webhook/", response={400: str, 200: str})
# def messenger_webhook(request, body: MessengerBody):
#     # import pdb; pdb.set_trace()
#     if body.object == "page":
#         return 200, 'Event Received'
#     return 400, 'Invalid page body'
