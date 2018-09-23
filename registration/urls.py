from django.urls import path
from . import views


app_name = "registration"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.registration_detail, name="registration_detail"),
    path('<int:pk>/edit/', views.registration_edit, name="registration_edit"),
    path('new', views.register, name="register"),
    path('list', views.registration_history, name="registration_history"),
    path('thank_you', views.thank_you, name="thank_you")
]