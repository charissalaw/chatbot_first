from django.contrib import admin
from django.urls import path

from chatbot.api import api
from chatbot.views.webhooks.api import FacebookWebhookView
# use following when support for HTTP issue fixed in django ninja
#from webhooks.api_text_res import api_plain_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/webhooks/webhook', FacebookWebhookView.as_view(), name='webhook'),

    # use following when support for HTTP issue fixed in django ninja
    # path('api/', api.urls),
    # path('api/', api_plain_text.urls),
]
