"""hr_systems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hr_systems_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees', views.employee_list),
    path('employees/count', views.employee_list_count),
    path('employees/search/<str:query>', views.employee_list),
    path('employees/<int:id>', views.employee_by_id),
    path('vacations', views.vacations_list),
    path('vacations/count', views.vacations_list_count),
    path('vacations/search/<str:query>', views.vacations_list),
    path('vacations/<int:id>', views.vacations_by_id),
]
