from rest_framework import serializers
from api.models import Products, Carts, Review
from django.contrib.auth.models import User


class Productserial(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    discription = serializers.CharField()
    catagory = serializers.CharField()
    image = serializers.ImageField()


class ProductModelSerial(serializers.ModelSerializer):
    avg_rating = serializers.CharField(read_only=True)
    review_count = serializers.CharField(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CartsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Carts
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    comment = serializers.CharField(max_length=200)

    class Meta:
        model = Review
        fields = '__all__'
