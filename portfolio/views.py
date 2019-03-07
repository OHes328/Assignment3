from django.shortcuts import render

from .models import Portfolio

# Create your views here.
def mypage(request):
    return render(request, 'mypage.html')


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/mypage.html', {'portfolios': portfolios})