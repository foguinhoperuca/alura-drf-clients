from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from clients.serializers import ClientSerializer
from clients.models import Client


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'cpf']
    search_fields = ['cpf', 'name', 'rg']
    filterset_fields = ['active']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
