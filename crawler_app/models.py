from django.db import models

# Create your models here.


class crawl(models.Model):
    post_name = models.CharField(max_length=100)
    post_path = models.CharField(max_length=200)
    post_category = models.CharField(max_length=100)

    def __str__(self):
        return self.post_name


class box(models.Model):
# #     title = models.CharField(max_length=100,default="SOME STRING")
# #     mylist = models.ManyToManyField(crawl)
# #
# #     def __str__(self):
# #         return self.title
    id = models.IntegerField(default=1,null=False,primary_key=True)
    mylist = models.CharField(max_length=200,default="default")