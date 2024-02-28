from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req,'blog/index.html')

def all_posts(req):
    return HttpResponse("all posts page")

"""def post_detail(req):
    return HttpResponse("single post in detail")"""
