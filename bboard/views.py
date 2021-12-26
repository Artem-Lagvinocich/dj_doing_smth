from django.http import HttpResponse
from .models import Bb
from django.shortcuts import render


def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'index.html', {'bbs': bbs})


def zero_page(request):
    return HttpResponse('zero page')


def main(request):
    return HttpResponse('main page')
