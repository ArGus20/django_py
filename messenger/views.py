from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from messenger.models import Message

# --------------------------Home view-----------------------------

# def home(request: HttpRequest) -> HttpResponse:
#     num_messages = Message.objects.count()
#
#     return render(
#         request,
#         "messenger/home.html",
#         context={"num_messages": num_messages}
#     )


# class HomeView(View):
#     def get(self, request: HttpRequest):
#         num_messages = Message.objects.count()
#
#         return render(
#             request,
#             "messenger/home.html",
#             context={"num_messages": num_messages}
#         )


class HomeView(TemplateView):
    template_name = "messenger/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_messages'] = Message.objects.count()

        return context


# --------------------------List View =================================
# def message_list(request: HttpRequest) -> HttpResponse:
#     messages = Message.objects.all()
#
#     return render(
#         request,
#         "messenger/message_list.html",
#         context={"messages": messages}
#     )


class MessageListView(ListView):
    model = Message


