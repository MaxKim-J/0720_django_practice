# bookmark/views.py

from django.shortcuts import render
from bookmark.models import Bookmark
# ORM사용하기- 쿼리를 대체 - 그걸 뷰에서 함


# 루트 디렉토리 뷰함수
def home(request):
    Bookmark.objects.all() # 북마크의 인스턴스를 죄다 조회하겟다!
    return None