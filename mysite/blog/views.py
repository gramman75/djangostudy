from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist


def tagPage(request, tag):
    post_list = Post.objects.filter(tags__name=tag)
    archives = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render_to_response("tagPage.html", {"post_list": posts, 
                                               "archives": archives, 
                                               "tag": tag}
                                            , context_instance=
                                            RequestContext(request))

def posts(request):
    post_list = Post.objects.order_by("-created") 
    paginator = Paginator(post_list, 5)
    #paginator.orphans = 2
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render_to_response("postList.html",{'posts':posts, 'archives':post_list}
                                          ,context_instance = RequestContext(request))
# 127.0.0.1:8000/blog/
def post(request, pk):
    post = Post.objects.get(pk=pk)
    post_list = Post.objects.order_by("-created") 
    try:
        prev_post = Post.objects.filter(created__lt=post.created).order_by("-created")[0:1].get()
    except ObjectDoesNotExist: 
        prev_post = None

    try:
        next_post= Post.objects.filter(created__gt=post.created).order_by("created")[0:1].get()
    except ObjectDoesNotExist:
        next_post = None
    return render_to_response("postDetail.html",{'post' : post,
                                                 'prev_post':prev_post,
                                                 'next_post':next_post,
                                                 'archives':post_list}
                                               ,context_instance=RequestContext(request))
def search(request):
    searchword = request.GET.get("search_text")
    posts = Post.objects.filter(subject__contains=searchword)
    return render_to_response("searchResult.html", {'posts':posts},
                                                context_instance=RequestContext(request))
