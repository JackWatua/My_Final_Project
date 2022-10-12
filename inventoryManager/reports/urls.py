from django.urls import path

#import views

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.reports, name='reports'),\
    path('new_report/', views.new_report, name="new_report"),\
]


if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,\
        document_root = settings.MEDIA_ROOT)

