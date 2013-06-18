from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.views import tagPage
from django.views.generic import ListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    #url(r'^blog/archive/$',ListView.as_view(
    #                queryset = Post.objects.order_by("-created"),
    #                context_object_name='archives',
    #                template_name="archive.html")),
    
    url(r'^blog/$','posts'),
    #url(r'blog/(?P<pk>\d+)/$',DetailView.as_view(
    #                model=Post,
    #                context_object_name="post",
    #                template_name="postDetail.html")),
    url(r'blog/(?P<pk>\d+)/$','post'),
    url(r'blog/tag/(?P<tag>\w+)/$',tagPage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/search/$','search'),
    # url(r'^blog/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
)

urlpatterns += patterns('',
    url(r'^blog/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^blog/logout/$','django.contrib.auth.views.logout',{'template_name':'logout.html'}),
    url(r'^blog/signup/$','signup'),

    )
