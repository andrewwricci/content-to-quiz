from django.urls import path
from . import views

app_name = 'submit'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index')
]