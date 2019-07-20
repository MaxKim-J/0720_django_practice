# bookmark/views.py

from django.shortcuts import render

import bookmark
from bookmark.models import Bookmark
# ORM사용하기- 쿼리를 대체 - 그걸 뷰에서 함


# 루트 디렉토리 뷰함수
def home(request):
    urlList = Bookmark.objects.order_by('-title') # 오더바이 내림차순 정렬
    for i in urlList:
        print(i.title)
    urlCount = Bookmark.objects.all().count() # 쿼리셋 (리스트)에 객체를 담아서 온다
    return render(request, "bookmark/home.html", {"urlList": urlList, "urlCount": urlCount} )
    # html로 가라 변수들! 딕셔너리의 키값은 html에서의 변수명
    # 값은 앞서 뷰함수에서 정의한 변수. 딕셔너리에 담아서 보내준다
    # render(리퀘스트, 템플릿, 템플릿에 줄 변수)


# 폼 뷰함수
def form(request):
    rqst = request.GET #템플릿에서 get 형태로 들어온 값의 리퀘스트를 받는다
    return render(request, "bookmark/form.html", {'ctx' : rqst} )