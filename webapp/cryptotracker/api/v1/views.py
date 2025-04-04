from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .utils import fetch_metadata_from_coingecko
from cryptotracker.models import Cryptocurrency
from .serializers import CryptocurrencySerializer


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    """
    ViewSet providing CRUD operations for Cryptocurrency.
    The create method is overridden to fetch and store metadata from Coingecko API.
    A custom action is provided to refresh metadata for all cryptocurrencies.
    """

    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

    def create(self, request, *args, **kwargs):
        symbol = request.data.get("symbol", "").lower()
        if not symbol:
            return Response(
                {"error": "Field 'symbol' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Get metadata from Coingecko
        metadata = fetch_metadata_from_coingecko(symbol)
        request.data["metadata"] = metadata
        # If name is not provided, fill it from metadata
        if not request.data.get("name"):
            request.data["name"] = metadata.get("name", "")
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=["post"], url_path="refresh")
    def refresh_metadata(self, request):
        """
        Custom endpoint for updating metadata of all cryptocurrencies.
        """
        cryptos = Cryptocurrency.objects.all()
        for crypto in cryptos:
            metadata = fetch_metadata_from_coingecko(crypto.symbol)
            crypto.metadata = metadata
            crypto.name = metadata.get("name", crypto.name)
            crypto.save()
        return Response({"status": "Metadata updated."}, status=status.HTTP_200_OK)
