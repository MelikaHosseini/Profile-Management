import django_filters
from .models import *
class searchUserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username' : ['exact'],
        }   
