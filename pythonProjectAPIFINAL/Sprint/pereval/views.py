import django_filters
from rest_framework import viewsets

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework import generics
from rest_framework import mixins

from .filters import PerevalFilter
from .serializers import *
from .models import *

class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class PerevalListView(ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_class = PerevalFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]



class CreateListView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):

    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user__email"]


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetRetrieveView(RetrieveUpdateAPIView):

    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError('Статус не "new"')
            serializer.save()
            return Response({'state': 1, 'message': 'Запись успешно изменена'})
        else:
            return Response({'state': 0, 'message': serializer.errors})



