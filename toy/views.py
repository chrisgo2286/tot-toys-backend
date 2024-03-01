from rest_framework import viewsets
from .serializers import ToySerializer
from .models import Toy
from django.db.models import Q

class ToyView(viewsets.ModelViewSet):
    serializer_class = ToySerializer
    queryset = Toy.objects.all()  

    def get_queryset(self):
        search_text = self.request.query_params.get('search')
        if search_text:
            filtered_queryset = self.queryset.filter(
                Q(name__icontains = search_text) | 
                Q(description__icontains = search_text)
            )
            return filtered_queryset
        return self.queryset