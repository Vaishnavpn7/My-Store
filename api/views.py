from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products, Carts, Review
from api.serializers import Productserial, ProductModelSerial, UserSerialize, CartsSerializer, ReviewSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import authentication, permissions


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Products.objects.all()
        serializer = Productserial(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serialize = Productserial(data=request.data)
        if serialize.is_valid():
            Products.objects.create(**serialize.validated_data)
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)


class ProductdetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Products.objects.get(id=id)
        sterialize = Productserial(qs, many=False)
        return Response(data=sterialize.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        Products.objects.filter(id=id).update(**request.data)
        qs = Products.objects.get(id=id)
        sterialize = Productserial(qs, many=False)
        return Response(data=sterialize.data)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        qs = Products.objects.get(id=id).delete()

        return Response(data='delete product')


class ProductViewViewset(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        qs = Products.objects.all()
        serialize = ProductModelSerial(qs, many=True)
        return Response(data=serialize.data)

    def create(self, request, *args, **kwargs):
        serialize = ProductViewViewset(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = Products.objects.get(id=id)
        serialize = ProductModelSerial(qs, many=False)
        return Response(data=serialize.data)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        Products.objects.filter(id=id).delete()
        return Response('deleted')

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        obj = Products.objects.get(id=id)
        serialize = ProductModelSerial(data=request.data, instance=obj)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

    @action(methods=['GET'], detail=False)
    def catagory(self, request, *args, **kwargs):
        ras = Products.objects.values_list('catagory', flat=True).distinct()
        return Response(data=ras)


class ProductViewViewsetmodel(viewsets.ModelViewSet):
    serializer_class = ProductModelSerial
    queryset = Products.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def catagory(self, request, *args, **kwargs):
        ras = Products.objects.values_list('catagory', flat=True).distinct()
        return Response(data=ras)

    @action(methods=['POST'], detail=True)
    def addto_cart(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        item = Products.objects.get(id=id)
        user = request.user
        user.carts_set.create(product=item)
        return Response(data='item added to cart')

    @action(methods=['POST'], detail=True)
    def add_review(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get('pk')
        item = Products.objects.get(id=id)

        serialize = ReviewSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save(product=item, user=user)
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

    @action(methods=['GET'], detail=True)
    def review(self, request, *args, **kwargs):
        product = self.get_object()
        qs = product.review_set.all()
        serialize = ReviewSerializer(qs, many=True)
        return Response(data=serialize.data)


class Userview(viewsets.ModelViewSet):
    # def create(self, request, *args, **kwargs):
    #     serialize = UserSerialize(data=request.data)
    #     if serialize.is_valid():
    #         serialize.save()
    #         return Response(serialize.data)
    #     else:
    #         return Response(serialize.errors)
    serializer_class = UserSerialize
    queryset = User.objects.all()


class Cartsview(viewsets.ModelViewSet):
    serializer_class = CartsSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     qs = request.user.carts_set.all()
    #     serializer = CartsSerializer(qs, many=True)
    #     return Response(data=serializer.data)

    # easy way down

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)


class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_review(self):
        return Review.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        Review.objects.get(id=id).delete()
        return Response(data='deleated')
