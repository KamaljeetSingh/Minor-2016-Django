from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from Cards import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('Cards.urls')),
    url(r'^api/', views.Cardlist.as_view()),
    url(r'^Home/',include('Home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns= format_suffix_patterns(urlpatterns)