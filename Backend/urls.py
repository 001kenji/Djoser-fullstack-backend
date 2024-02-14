
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base  import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #path('gest/', TemplateView.as_view(template_name='index.html'))
]


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

