from crawler_app.models import crawl,box
from rest_framework import serializers



class CelebSerializer(serializers.HyperlinkedModelSerializer):
    #Celeb = serializers.ImageField(use_url = True)


    class Meta:
        model = crawl
        fields=['id','post_name','post_path','post_category',]

class RacingModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = box
        fields=['id','mylist']


