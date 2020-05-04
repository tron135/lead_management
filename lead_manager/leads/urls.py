from django.urls import path

from . import views

app_name='leads'
urlpatterns = [
    path('', views.home, name='home'),
    path('leads/', views.lead, name='leads')
]
