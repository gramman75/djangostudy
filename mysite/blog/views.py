from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def tagPage(request, tag):
    post = Post.objects.filter(tags__name=tag)
    return render_to_response("tagPage.html", {"post_list" : post,
                                               "tag" : tag}
                                            , context_instance=RequestContext(request))

def posts(request,page=1):
    post_list = Post.objects.order_by("-created") 
    paginator = Paginator(post_list,2)
    #paginator.orphans = 2
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render_to_response("postList.html",{'posts':posts}
                                          ,context_instance = RequestContext(request))