from django.urls import path
from . import views

urlpatterns = [
    path('sessions', views.sessions, name='sessions'), 
    path('one_session/<str:id>', views.one_session, name='one_session')
]