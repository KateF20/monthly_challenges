from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='all-challenges'),
    path('<int:month>', views.num_redirect, name='num_redirect'),
    path('<str:month>', views.monthly_challenges, name='monthly-challenge'),
]
