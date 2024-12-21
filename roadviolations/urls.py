"""
URL configuration for roadviolations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from road import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    
    path('violations/', views.RoadViolationListView.as_view(), name='violation-list'),
    path('violations/create/', views.RoadViolationCreateView.as_view(), name='violation-create'),
    path('violations/<int:pk>/edit/', views.RoadViolationUpdateView.as_view(), name='violation-edit'),
    path('violations/<int:pk>/delete/', views.RoadViolationDeleteView.as_view(), name='violation-delete'),
]
