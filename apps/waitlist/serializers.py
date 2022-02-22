from rest_framework import serializers
from .models import Waitlist


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ('id', 'first_name', 'last_name', 'email',
                  'created_at', 'updated_at')
