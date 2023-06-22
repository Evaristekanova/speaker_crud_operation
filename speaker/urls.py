from django.urls import path
from . import views

urlpatterns = [
    path('', views.speaker_list),
    path('<int:id>/', views.speaker_details),
    path('<int:id>/delete/', views.delete_speaker)
]