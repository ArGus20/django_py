from django.urls import path

from messenger.views import home


app_name = 'messenger'

urlpatterns = [
    path('home/', home, name='home')
]
