from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework import viewsets

class Userapiview(APIView):
    def get(self,request):
        queryset=User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response({"ok":True,"members":serializer.data},status=status.HTTP_200_OK)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class updateapi(APIView):
    def get_object(self,user_id):
        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,user_id):
        user=self.get_object(user_id)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,user_id):
        user=self.get_object(user_id)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,user_id):
        user=self.get_object(user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""//////////////////antother approch for getting the data////////////////"""

class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

