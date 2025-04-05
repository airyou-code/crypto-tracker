from rest_framework import serializers
from cryptotracker.models import Cryptocurrency


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ("symbol", "name", "metadata")
