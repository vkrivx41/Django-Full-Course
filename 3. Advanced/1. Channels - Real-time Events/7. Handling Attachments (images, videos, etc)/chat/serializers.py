from rest_framework import serializers

from chat.models import Message
from utilities.s3 import cloudfront

# Create the message serializer (with attachment url serilaizer model field that gets the download url)
class MessageSerializer(serializers.ModelSerializer):
    attachment_url = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ['sender', 'created_at']

    def get_attachment_url(self, obj):
        if not obj.attachment:
            return None
        
        return cloudfront.generate_signed_url(obj.attachment)
