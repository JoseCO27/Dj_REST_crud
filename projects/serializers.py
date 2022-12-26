from rest_framework import serializers
from .models import Project # django va a saber que responder a las peticiones GET, PUT, DELETE

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        # solo campo de lectura.
        read_only_fields = ('created_at',)  
        # quien puede consultar y que peticiones se pueden hacen

        #verbose_name = 'ModelName'
        #verbose_name_plural = 'ModelNames'


