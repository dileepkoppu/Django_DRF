from rest_framework.response import Response
from rest_framework import generics,filters,permissions
from rest_framework.decorators import api_view
from rest_framework.compat import distinct

from .serializers import UserSerializers,contactSerializers
from . models import contact





class homefilter(filters.SearchFilter):


    def filter_queryset(self, request, queryset, view):
        search_fields = ['phone_number','name']
        search_terms = self.get_search_terms(request)
        if (not search_fields or not search_terms):
            return queryset
        elif len(search_terms)!=1:
            return queryset.objects.none()
        base=queryset
        if not (search_terms[0].isdigit()):
            queryset=queryset.filter(name__startswith=search_terms)

        else:
            queryset1=queryset.filter(phone_number__exact=search_terms[0],registered=True)
            if queryset1:
                queryset=queryset1
            else:
                queryset=queryset.filter(phone_number__icontains=search_terms[0]).only('name','id')
        if self.must_call_distinct(queryset, search_fields):
            queryset = distinct(queryset, base)
        return queryset



@api_view(['GET'])
def welcome(request):
    return Response({
		'Create':'/signup/',
        'login':'/api-auth//login/',
		'List of contact':'/home/',
		'Update':'/update/<int:pk>/',
})

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializers


class updateView(generics.UpdateAPIView):
    permission_classes =[permissions.IsAuthenticated]
    queryset = contact.objects.all()
    serializer_class = contactSerializers


class homeListView(generics.ListAPIView):
    queryset = contact.objects.all()
    serializer_class = contactSerializers
    permission_classes =[permissions.IsAuthenticated]
    filter_backends = [homefilter]
    search_fields = ['phone_number','name']