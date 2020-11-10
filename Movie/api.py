from rest_framework import generics
from .models import Profile,Category,Movie,Rate
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginAdminSerializer,UserSerializer,LoginSerializer,profileSerializer,CategorySerializer,MovieSerializer,RateSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from knox.models import AuthToken
from rest_framework import  permissions
from django.core.paginator import Paginator

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
    })
class LoginAdminAPI(generics.GenericAPIView):
  serializer_class = LoginAdminSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
   
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
    })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
   
    def get_object(self):
        return self.request.user


@api_view(['GET', 'POST'])
def Profile_list(request,pk):

    if request.method == 'GET':
        items = Profile.objects.all()
        paginator = Paginator(items, 30)
        users = paginator.page(pk)

        serializer = profileSerializer(users,context={'request': request} ,many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def Profile_detail(request, pk):

    try:
        items = Profile.objects.get(pk=pk)
    except items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print("item",items.deleted)
        serializer = profileSerializer(items,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = profileSerializer(items, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        items.deleted=True
        print("item",items.deleted)
        items.save()

        
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def categori_list(request):

    if request.method == 'GET':
        items = Category.objects.all()
        serializer = CategorySerializer(items,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):

    try:
        items = Category.objects.get(pk=pk)
    except items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(items,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(items, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Movie_list(request):

    if request.method == 'GET':
        items = Movie.objects.all()
        paginator = Paginator(items, 30)
        mi = paginator.page(pk)
        serializer = MovieSerializer(mi,context={'request': request} ,many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def Movie_detail(request, pk):

    try:
        items = Movie.objects.get(pk=pk)
    except items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(items,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(items, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)