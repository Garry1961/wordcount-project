

from django.urls import path
from.import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Count/', views.count, name='count'),
    path('About/', views.about, name='about'),
    
   
]
