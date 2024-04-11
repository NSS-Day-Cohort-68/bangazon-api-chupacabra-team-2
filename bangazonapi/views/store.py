from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from bangazonapi.models import Store, Product, StoreProduct, Customer
from .product import ProductSerializer
from .storeproduct import StoreProductSerializer

from django.contrib.auth.models import User


class StoreSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "seller",
            "description",
            "product_count",
            "is_owner",
            "products",
        ]

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.seller


class StoreView(viewsets.ViewSet):
    def list(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            store = Store.objects.get(pk=pk)
            serializer = StoreSerializer(store, context={"request": request})
            return Response(serializer.data)
        except Store.DoesNotExist:
            return ResourceWarning(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        current_user = request.user

        try:
            open_store = Store.objects.get(seller=current_user)
        except Store.DoesNotExist:
            open_store = Store()
            open_store.name = request.data["name"]
            open_store.description = request.data["description"]
            open_store.product_count = 0
            open_store.seller = current_user
            open_store.save()

        store_product = StoreProduct()
        store_product.product = Product.objects.get(pk=request.data["product_id"])
        store_product.store = open_store
        store_product.save()

        return Response({}, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=False)
    def store_products(self, request):

        if request.method == "GET":
            store_products = Product.objects.filter(store.id == store_products.store_id)
            serializer = StoreProductSerializer(
                store_products, many=True, context={"request": request}
            )
            return Response(serializer.data)
