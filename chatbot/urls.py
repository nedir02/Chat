from django.urls import path
from chatbot.views import home, get_response

urlpatterns = [
   path("", home, name="home"),
   path("get_response/", get_response, name="get_response"),
]