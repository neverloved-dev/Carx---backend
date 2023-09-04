from .models import OrdinaryUser
from rest_framework import serializers,validators

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdinaryUser
        fields = ('first_name','last_name','phone_number','email')


    def create(self,validated_data):
        firstName = validated_data['first_name']
        lastName = validated_data["last_name"]
        #email = validated_data["email"]
        phoneNumber = validated_data["phone_number"]
        user = OrdinaryUser.objects.create (  
            # first_name = firstName,
            # last_name = lastName,
            # email = email,
            # phone_number = phoneNumber
            **validated_data
        )
          
        
        return user