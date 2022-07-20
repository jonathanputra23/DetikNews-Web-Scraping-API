from urllib import response
from django.http import JsonResponse
from .models import webSite
from .serializer import searchKeywordsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .function import scrape_function


@api_view(['POST'])
def scrapeWebsite(request, format=None):
    """Using the payload and scrape DetikNews result based on the payload"""
    
    if request.method == 'POST':
        serializer = searchKeywordsSerializer(data=request.data)
        if serializer.is_valid():
            query = scrape_function.search_website(serializer.data)
            result = scrape_function.scrape_website(query)

            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def getURL(request, format=None):
    """Using the payload and get the complete DetikNews URL"""
    
    if request.method == 'POST':
        serializer = searchKeywordsSerializer(data=request.data)
        if serializer.is_valid():
            query = scrape_function.search_website(serializer.data)

            return Response(query, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)