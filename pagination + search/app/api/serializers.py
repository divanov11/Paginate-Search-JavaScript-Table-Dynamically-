from rest_framework import serializers
from app.models import *
import time

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

	