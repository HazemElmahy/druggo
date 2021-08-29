from django.urls import path
from core import views

urlpatterns = [
    path('hello/', views.number_list),
    #path('hello/<int:pk>/', views.snippet_detail),
]