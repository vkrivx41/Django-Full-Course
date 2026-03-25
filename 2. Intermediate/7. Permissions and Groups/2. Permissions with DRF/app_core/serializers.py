from rest_framework import serializers

from app_core.models import Document, User, Subscription


    

class MeSerializer(serializers.ModelSerializer):
    class SubscriptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Subscription
            fields = ('type', 'joined_at', 'ends_at')
            
    subscription = SubscriptionSerializer()
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'subscription', 'permissions')

    
    def get_permissions(self, obj):
        return list(obj.get_all_permissions())


class DocumentSerializer(serializers.ModelSerializer):
    additional = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ('id', 'title', 'content', 'owner', 'created_at', 'additional')
        read_only_fields = ('id',)


    def get_additional(self, obj) -> bool:
        user = self.context.get('request').user

        if user.has_perm('app_core.publish_document'):
            return "Confidential data for premium users"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user = self.context.get('request').user

        if not user.has_perm('app_core.publish_document'):
            self.fields.pop('additional', None)