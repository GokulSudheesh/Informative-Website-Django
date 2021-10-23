from django.urls import path

from . import views

app_name = 'info'

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.survey, name='survey'),
    path('reviews/', views.reviews, name='reviews'),
    path('submit/', views.submit, name='submit')
]