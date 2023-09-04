from .forms import UserRegistrationForm
from . import models
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserRegisterSerializer
# Create your views here.

@api_view(["POST"])
def register_api(request):
    serializer = UserRegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.save()
    return HttpResponse({
        "user info":{
            'id': user.id,
             'firstName': user.first_name,
             'lastName': user.last_name,
             'email': user.email,
             'phone_number': user.phone_number,
        }
    })


@api_view(["GET"])
def test_api(request):
    return HttpResponse("This is a test")

