
from django.urls import path
from .views import UserAPIView,LoginView

urlpatterns = [
    path("",UserAPIView.as_view()),
    path("login/",LoginView.as_view())

]
