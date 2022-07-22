from django.contrib import admin
from django.urls import path
from . import views

app_name = 'orbit_display'

urlpatterns = [
    path('', views.CheckedBodiesView.as_view(), name='welcome_vis'),
    path('plot/<str:objects>/', views.plot_orbits, name='plot'),
]
