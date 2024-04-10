from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from bangazonapi.models import Store
from .product import ProductSerializer


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


class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
