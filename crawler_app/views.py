from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CelebSerializer,RacingModelSerializer
from .models import crawl,box
from .racing import racingmodel_list
#-------------------------#
from background_task import background
from django.utils import timezone

class crawlViewSet(viewsets.ModelViewSet):

    queryset = crawl.objects.all()
    serializer_class = CelebSerializer

    # def create(self,request,pk=None):
    #     RacingModel = "RacingModel"
    #     names=[]
    #     cnt=1
    #     if RacingModel == request.data['post_category']:
    #         link = racingmodel_list()
    #         for area in link:
    #             for v in area.find_all("div","wiki-heading-content"):
    #                 for b in v.find_all("li")[2:]:
    #                     names.append(b.text.split('[')[0])
    #     for t in names:
    #         box(mylist=t,id=cnt).save()
    #         cnt+=1
    #     return Response(names)
    def create(self,request,pk=None):
        cnt=1
        mymodel = request.data['post_category']
        slist(mymodel,schedule=timezone.now())
        return Response("ok")


    # def get(self,request,pk=None):
    #
    #     if request.method == 'GET':
    #         queryset = box.objects.all()
    #         serializer_class = RacingModelSerializer(queryset,many=True)
    #         return Response(serializer_class.data)


@background(schedule=60)
def slist(request):
    RacingModel = "레이싱 모델"
    names=[]
    cnt=1
    if RacingModel == request:
        link = racingmodel_list(RacingModel)
        for area in link:
            for v in area.find_all("div","wiki-heading-content"):
                for b in v.find_all("li")[2:]:
                    names.append(b.text.split('[')[0])
    print(">>>>",names)

    for t in names:
        box(mylist=t,id=cnt).save()
        cnt+=1




