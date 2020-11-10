import numpy as np 
from rest_framework import serializers 
from rest_framework.response import Response
from django.conf import settings 
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Movie

class Rate_RS:
    def __init__(self, item):

        self.item = item

class Rate_RS_Serializer(serializers.Serializer):

    item = serializers.ListField()
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Movie
        fields = '__all__'
    
@api_view(('GET',))
def recomend(request,UID):
    movie=[]
    ALLmovie = Movie.objects.all()
    for i in ALLmovie:
        movie.append(i.id)
    if request.method == 'GET':
        print("ok")
        try:
            approx_R_i = settings.U[UID-1].dot(settings.V.T) 
        # tam =Rate_RS(item=approx_R_i)
            list_film=(approx_R_i.argsort()[-10:][::-1])
        except :
            
            list_film= np.random.randint(3000, size=(10))

        ara = []
        for i in list_film:
            items = Movie.objects.get(pk=movie[i])
            ara.append(items)
        serializer = MovieSerializer(ara,context={'request': request} ,many=True)
        # print(ser.data)
        
        return Response(serializer.data)
    
    # list_film=(approx_R_i.argsort()[-5:][::-1]) 
