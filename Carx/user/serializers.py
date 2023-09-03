from .models import UserAccount
from rest_framework import serializers,validators

class UserRegisterSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields =  fields = ('first_name','last_name','phone_number','email')


    def create(self,validated_data):
        firstName = validated_data["firstName"]
        lastName = validated_data["lastName"]
        email = validated_data["email"]
        phoneNumber = validated_data["phoneNumber"]
        user = UserAccount.objects.create(  
            first_name = firstName
            last_name = lastName
            email = email
            phone_number = phoneNumber)
          
        
        return user