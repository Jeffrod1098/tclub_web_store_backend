from rest_framework import serializers
from .models import Item,Cart,CartItem,Comment


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Item
        fields = ('id', 'name', 'price', 'details', 'photo_1_url', 'photo_2_url',)

class CartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cart 
        fields = ('id', 'quantity')

class CartItemSerializer(serializers.HyperlinkedModelSerializer):

    cartId = CartSerializer()
    itemId = ItemSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'cartId', 'itemId', 'quantity')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    item = ItemSerializer()

    class Meta:
        model= Comment
        fields = ('title', 'content', 'item', 'created')