from django.urls import path
from . import views

urlpatterns = [
    ##sets the url path to home page CarMaintenanceTracker_home.html.
    path('', views.carMaintenanceTrackerHome, name='CarMaintenanceTracker_home'),
    path('CarMaintenanceTracker_history/', views.viewHistroy, name='CarMaintenanceTracker_history'),
    path('CarMaintenanceTracker_create/', views.addEvent, name='CarMaintenanceTracker_create'),
    path('CarMaintenanceTracker_account/', views.account, name='CarMaintenanceTracker_account'),
    path('<int:pk>/CarMaintenanceTracker_details/', views.details, name='CarMaintenanceTracker_details'),
]
