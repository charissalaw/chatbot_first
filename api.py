from ninja import NinjaAPI, Schema, Form
from ninja.renderers import BaseRenderer


api = NinjaAPI()

# use following when http issue resolved with Django Ninja
# api.add_router("/webhooks", webhook_router)
