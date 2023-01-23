from django.urls import path
from owner import views

urlpatterns = [

    path("register", views.SignupView.as_view()),
    path('home', views.HomeView.as_view()),
    path('login', views.SigninView.as_view()),
    path('addproduct', views.ProductCreateView.as_view())

]
