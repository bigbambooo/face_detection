from rest_framework import serializers

from api.models.image import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        #fields = ('request_id', 'callback_url', 'date_created')
        fields = ('status', 'date_created')
