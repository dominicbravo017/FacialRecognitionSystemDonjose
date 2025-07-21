from rest_framework import serializers
from .models import Person
import base64

class PersonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_upload = serializers.CharField(
        write_only=True, required=False, allow_blank=True, allow_null=True
    )

    class Meta:
        model = Person
        fields = ['id', 'name', 'role', 'position', 'timestamp', 'image', 'image_upload']

    def get_image(self, obj):
        if obj.image:
            return base64.b64encode(obj.image).decode('utf-8')
        return None

    def create(self, validated_data):
        image_file = self.context['request'].FILES.get('image')
        image_bytes = image_file.read() if image_file else None
        validated_data['image'] = image_bytes
        return Person.objects.create(**validated_data)
