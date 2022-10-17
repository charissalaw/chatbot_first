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

# this is the only view not using Django-Ninja. See commented code below for detail
class FacebookWebhookView(View):
    @method_decorator(csrf_exempt) # required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) #python3.6+ syntax

    def get(self, request, *args, **kwargs):
        hub_mode   = request.GET.get('hub.mode')
        hub_token = request.GET.get('hub.verify_token')
        hub_challenge = request.GET.get('hub.challenge')
        if hub_token != VERIFY_TOKEN:
            return HttpResponse('Error, invalid token', status=403)
        return HttpResponse(hub_challenge)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        if body['object'] == 'page':
            return HttpResponse('Event Received', status=200)
        return HttpResponse('Invalid page body', status=400)
