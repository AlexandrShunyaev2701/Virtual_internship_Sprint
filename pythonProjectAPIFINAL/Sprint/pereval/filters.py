from django_filters import rest_framework as filters
from .models import Pereval

class PerevalFilter(filters.FilterSet):
    user__email = filters.CharFilter(field_name='user__email')

    class Meta:
        model = Pereval
        fields = ['user__email']