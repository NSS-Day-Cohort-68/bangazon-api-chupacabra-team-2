from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from bangazonapi.models import Store, Product, StoreProduct


class StoreProductSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product category"""

    class Meta:
        model = StoreProduct
        url = serializers.HyperlinkedIdentityField(
            view_name="storeproducts-detail", lookup_field="id"
        )
        fields = ("id", "url", "store", "product")


class StoreProducts(viewsets.ViewSet):

    def list(self, request):
        store_product = StoreProduct.objects.all()

        serializer = StoreProductSerializer(
            store_product, many=True, context={"request": request}
        )
        return Response(serializer.data)
