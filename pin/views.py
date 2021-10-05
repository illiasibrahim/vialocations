from django.http import HttpResponse
import os
from .models import Pincode
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import PincodeSerializer

# Create your views here.

def add(request):
    f = open("IN.txt", encoding = 'utf-8')
    try:
        line = f.readlines()
        for item in line:
            location = item.split('\t')
            print(location[1],'....',location[7],'....',location[9],'.....',location[10])
    finally:
        f.close()
    return HttpResponse('hello world')



def results(request):
    module_dir = os.path.abspath('./pin/')  
    file_path = os.path.join(module_dir, 'IN.txt')
    data_file = open(file_path , 'r') 
    line = data_file.readlines()
    coordinate = '{lat},{lng}'
    count = 0
    for item in line:
        if count > 160000:
            location = item.split('\t')
            coordinates = coordinate.format(lat=location[9],lng=location[10])
            place = location[2]
            pin = location[1]
            region = location[7]
            pincode = Pincode(pin=pin,region=region,place=place,coordinates=coordinates)
            pincode.save()
            print(count,' success')
        else:
            print(count)
        count += 1
        
    return HttpResponse('hello world')

class PincodeList(generics.ListAPIView):
    serializer_class = PincodeSerializer

    def get_queryset(self):
        pin = self.request.query_params.get('pin')
        queryset = Pincode.objects.filter(pin=pin)
        if queryset:
            return queryset
        return None

    def get(self, request):
        try:
           data=PincodeSerializer(self.get_queryset(),many=True).data
           context = {
               "data" : data,
               "message" : "Contents returned successfully",
               "success" : True
               }
           return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
           context = {'error': str(error), 'success': "false", 'message': 'Failed To Get contents.'}
           return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetPincodes(generics.ListAPIView):
    serializer_class = PincodeSerializer
    queryset = Pincode.objects.all()