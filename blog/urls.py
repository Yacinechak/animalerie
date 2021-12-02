from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
    path('animal/<str:id_animal>/?<str:message>', views.animal_detail, name='animal_detail_mes'),
]
