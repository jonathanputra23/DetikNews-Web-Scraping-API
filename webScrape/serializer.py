from rest_framework import serializers
from .models import webSite

class searchKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = webSite
        fields = ['keywords', 'site', 'fromDate', 'toDate', 'page']