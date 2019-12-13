from rest_framework import serializers
from antrian.models import Queue
from merchant.models import Makanan, Merchant
from login.models import quotes

class QueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Queue
        fields = ('user', 'nama_makanan', 'status', 'foto')


class MakananSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Makanan
        fields = ('merchant', 'nama', 'deskripsi', 'foto')


class MerchantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Merchant
        fields = ('nama_merchant', 'desc', 'link_gambar',)

class QuotesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = quotes
        fields = ('quotes',)
