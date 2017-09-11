from django.conf.urls import include, url
from django.contrib import admin
from recipes import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='RecipePost')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
