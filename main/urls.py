from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:performance_data_id>/', views.detail, name='detail'),
]