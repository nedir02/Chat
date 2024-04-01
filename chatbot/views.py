from django.shortcuts import render
from chaterbot import Chatbot

# Create your views here.
chatbot = Chatbot("Payhasly")


def home(request):
    return render(request, 'chatbot/home.html')


def get_response(request):
    user_input = request.GET.get("user_input", "")
    response = str(chatbot.get_response(user_input))
    return render(request, "chatbot/home.html", {"user_input": user_input, "response": response})