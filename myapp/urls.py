from django.urls import path
from .views import CareerList, CareerListCreate, CareerPartialUpdate, CareerRetrieveUpdateDestroy, CareerDestroy

urlpatterns = [
    path('careers/', CareerList.as_view(), name='career-list'),  # URL para GET e POST
    path('careers/<int:pk>/', CareerRetrieveUpdateDestroy.as_view(), name='career-retrieve-update-destroy'),  # URL para GET, PUT, DELETE
    path('careers/<int:pk>/', CareerPartialUpdate.as_view(), name='career-partial-update'),  # URL para PATCH
]