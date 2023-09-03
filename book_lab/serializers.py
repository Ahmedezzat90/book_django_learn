from rest_framework import serializers
from .models import publishing_house,book


class publishing_houseserializer(serializers.ModelSerializer):
    class Meta:
        model = publishing_house
        fields = ('name','id')

class bookserializer(serializers.ModelSerializer):
    publishing_house = publishing_houseserializer(read_only=True)
    publishing_house_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = book
        fields = ("name",
            "publish_date",
            "isbn",
            "publishing_house","publishing_house_id")
