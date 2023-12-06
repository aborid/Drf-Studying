
from django.urls import path
from .views import CartAPIView, CartDetailView, UpdateCartNumAPIView,CartCountAPIView,DeleteCartGoodsAPIView

urlpatterns = [
    path('',CartAPIView.as_view()),
    path('detail/',CartDetailView.as_view()),
    path('num/',UpdateCartNumAPIView.as_view()),
    path('counts/', CartCountAPIView.as_view()),
    path('delete/', DeleteCartGoodsAPIView.as_view())
]