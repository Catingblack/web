from django.urls import url

from . import views

urlpatterns = [
    path('', views.test, name='test'),
]