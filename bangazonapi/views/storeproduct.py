from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from bangazonapi.models import store, product, storeproduct


class StoreProductSerializer(serializers.ModelSerializer):
    """JSON serializer for product category"""

    class Meta:
        model = storeproduct
        fields = ("id", "store", "product")


class StoreProducts(viewsets.ViewSet):

    def list(self, request):
        store_product = StoreProducts.objects.all()

        serializer = StoreProductSerializer(
            store_product, many=True, context={"request": request}
        )
        return Response(serializer.data)
