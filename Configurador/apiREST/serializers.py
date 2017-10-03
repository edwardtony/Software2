from rest_framework import serializers
from apiREST.models import *

class CharacterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Character
		fields = '__all__'