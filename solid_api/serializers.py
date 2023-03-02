from rest_framework import serializers
from . import models

#class drinkserializers(serializers.Serializer):
#    id = serializers.IntegerField()
#    name = serializers.CharField()
#    company = serializers.CharField()
#    quantity = serializers.IntegerField()
#    prize = serializers.FloatField()
#    discount = serializers.IntegerField()
#
#    def create(self, data):
#        return models.drinks.objects.create(**data)
#
#    def update(self, instance, validated_data):
#        instance.id = validated_data.get('id',instance.id)
#        instance.name = validated_data.get('name',instance.name)
#        instance.company = validated_data.get('company',instance.company)
#        instance.quantity = validated_data.get('quantity',instance.quantity)
#        instance.prize = validated_data.get('prize',instance.prize)
#        instance.discount = validated_data.get('discount',instance.discount)
#        instance.save()
#        return instance

class drinkserializers(serializers.ModelSerializer):
    class Meta:
        model = models.drinks
        fields = '__all__'