from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('user-details',views.user_details,name='user_details'),
    path('user-details-api',views.user_details_api,name='user_details_api'),
]