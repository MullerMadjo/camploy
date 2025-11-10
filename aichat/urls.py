 
from django.urls import path
from . import views

urlpatterns = [
    path("chat-ai/", views.camploy_ai_chat_view, name="camploy_ai_chat"),
    path("chat-ai/api/", views.camploy_ai_chat_api, name="camploy_ai_chat_api"),
    # path("clear/", views.clear_chat, name="clear_chat"),
]
