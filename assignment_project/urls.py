from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('', views.home, name='home'),
    path('level1/', include('level1.urls')),
    path('level2/', include('level2.urls')),
    path('level3/', include('level3.urls')),
]
