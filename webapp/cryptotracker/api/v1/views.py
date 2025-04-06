from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import (
    SessionAuthentication
)

from cryptotracker.models import Cryptocurrency
from .serializers import CryptocurrencySerializer
from .utils import handle_bitget_response
from bitget_api_python import Client
from django.conf import settings

client: Client = Client(
    api_key=settings.BITGET_API_KEY,
    api_secret=settings.BITGET_API_SECRET,
    api_passphrase=settings.BITGET_API_PASSPHRASE,
)


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    """
    ViewSet providing CRUD operations for Cryptocurrency.
    The create method is overridden to fetch and store metadata from Coingecko API.
    A custom action is provided to refresh metadata for all cryptocurrencies.
    """

    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    lookup_field = "symbol"
    lookup_value_regex = "[a-zA-Z0-9_]+"

    def create(self, request, *args, **kwargs):
        symbol = request.data.get("symbol", "").lower()
        if not symbol:
            return Response(
                {"error": "Field 'symbol' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Get metadata from Bitget API
        res = client.get_symbol_info(symbol)
        data: list = handle_bitget_response(res)
        if not data:
            return Response(
                {"error": f"Data for symbol '{symbol}' not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        request.data["metadata"] = data[0]
        # If name is not provided, fill it from metadata
        if not request.data.get("name"):
            request.data["name"] = data[0].get("baseCoin", "")
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=["post"], url_path="refresh")
    def refresh_metadata(self, request):
        """
        Custom endpoint for updating metadata of all cryptocurrencies.
        """
        cryptos = Cryptocurrency.objects.all()
        for crypto in cryptos:
            res = client.get_symbol_info(crypto.symbol)
            data: list = handle_bitget_response(res)
            if not data:
                return Response(
                    {"error": f"Data for symbol '{crypto.symbol}' not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            crypto.metadata = data[0]
            crypto.name = data[0].get("baseCoin", crypto.name)
            crypto.save()
        return Response({"status": "Metadata updated."}, status=status.HTTP_200_OK)
