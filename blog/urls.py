from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
    path("all_posts/",views.all_posts,name="all_posts"),
    path("all_posts/<slug:slug>",views.post_detail,name="post_detail")
]