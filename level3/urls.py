from django.urls import path
from . import views

urlpatterns = [
    path('verify_certificate/<str:token>/', views.verify_certificate, name='verify_certificate'),
]
