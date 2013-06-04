from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.views import tagPage
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    '''
    url(r'^blog/$',ListView.as_view(
                    queryset = Post.objects.order_by("-created"),
                    context_object_name='post_list',
                    template_name="postList.html")),
    '''
    url(r'blog/(?P<pk>\d+)/$',DetailView.as_view(
                    model=Post,
                    context_object_name="post",
                    template_name="postDetail.html")),
    url(r'blog/tag/(?P<tag>\w+)/$',tagPage),
    url(r'^admin/', include(admin.site.urls)),
)
