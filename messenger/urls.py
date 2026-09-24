from django.urls import path

from messenger.views import HomeView, message_list

app_name = 'messenger'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path("messages/", message_list, name="message-list")
]
