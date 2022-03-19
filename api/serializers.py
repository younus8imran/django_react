from rest_framework import serializers  
from .models import Lead 

class LeadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lead 
		fields = ('id', 'name', 'age', 'image', 'email', 'message')
		fields = (
			"id",
			"name",
			"age",
			"get_image",
			"email",
			"message",
			)
	