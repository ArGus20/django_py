from django.urls import path

from messenger.views import HomeView,  MessageListView

app_name = 'messenger'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path("messages/", MessageListView.as_view(), name="message-list")
]
