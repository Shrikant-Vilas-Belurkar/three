from django.urls import path
from tracker import views

urlpatterns = [
    path('tracker/', views.tracker),
]
