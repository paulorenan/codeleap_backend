from rest_framework import generics
from .models import Career
from .serializers import CareerSerializer

class CareerList(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerListCreate(generics.CreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerPartialUpdate(generics.UpdateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerDestroy(generics.DestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer