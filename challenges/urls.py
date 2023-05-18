from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='all-challenges'),
    path('<int:month>', views.monthly_challenges_by_num, name='monthly-challenge-int'),
    path('<str:month>', views.monthly_challenges, name='monthly-challenge-str'),
]
