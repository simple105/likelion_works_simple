from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) #문자열 200자까지 입력하게해주는 껍데기
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]
# Create your models here.

