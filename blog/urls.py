from django.urls import path

from . import views

urlpatterns=[
    path('', views.BlogHomeView.as_view(), name='home'),
    path('add_post', views.PostAdd.as_view(), name='add_post'),
]