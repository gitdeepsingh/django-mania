from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# handle rest requests

# @api_view(['Get']) # dummy get user, no DB involved 
# def get_user(request):
#     return Response(UserSerializer({ 'name': 'Deep', 'age': 32 }).data)

@api_view(['Get'])
def get_users(request): # fetch from db
    users = User.objects.all()
    serializer = UserSerializer(users, many=True) #users => many
    return Response(serializer.data)

@api_view(['Post'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




