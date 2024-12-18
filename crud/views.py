from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework import status

# get all users
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

#get single user
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

#add user
@api_view(['POST'])
def addUser(request):
    print(request.data)
    serializer = UserSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update user
@api_view(['PUT'])
def updateUser(req,pk):
    user= User.objects.get(id=pk)
    serializer = UserSerializer(instance = user , data=req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#delete user
@api_view(['DELETE'])
def deleteUser(req,pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response("Item deleted Successfully !")