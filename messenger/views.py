from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from messenger.models import Message


def home(request: HttpRequest) -> HttpResponse:
    num_messages = Message.objects.count()

    return render(request, "messenger/home.html", context={"num_messages": num_messages})