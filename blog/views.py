from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects #쿼리셋:객체들을 받아오는 것  #method:객체처리 방법
    return render(request, 'blog.html', {'blogs':blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).method
    # .all(): 객체모두 반호나
    # .count() : 객체개수 반환
    # .first(): 첫번째객체 반환
    # .last(): 마지막객체 반환

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))
