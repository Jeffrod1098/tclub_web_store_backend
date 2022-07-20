from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from store_db.models import Item,Cart,CartItem,Comment
    
urlpatterns = [
    path('items', views.ItemList.as_view(), name='item_list'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('comments', views.CommentList.as_view(), name='comment_list' ),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('cartItemList/<int:pk>', views.CartItemDetail.as_view(), name='cartItem_list'),
    path('carts', views.CartList.as_view(), name='cart_list'),
]
