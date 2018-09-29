from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('card/', views.card_new, name='card_new'),
    # path('card/<int:pk>/', views.card_detail, name='card_detail'),
    path('card/detail/', views.card_detail, name='card_detail'),

]
