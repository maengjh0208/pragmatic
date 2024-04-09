from django.urls import path

from accountapp.views import hello_word

app_name = "accountapp"

urlpatterns = [
    path('hello_word/', hello_word, name='hello_word')
]
