from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import url
from django.urls import include,path,re_path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    path('photos/',include('photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
