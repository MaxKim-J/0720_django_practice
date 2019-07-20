from django.db import models

# Create your models here.



class Bookmark(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField("url", unique=True)
    # null - 필드에 자체에 Null값 허용, 쿼리를 통해 빈값을 저장할 수 있음
    # blank - 필드에 empty값 허용, 필드가 폼에서 빈 채로 저장되는 것을 허용
    # unique - 유일성 여부, 같은 내용이 db에 올라오지 못함. sql에서는 유니크 인덱스 만들어짐
