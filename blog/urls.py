from django.contrib import admin
from django.urls import path, include
from about.views import homepage, blog, maqola, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', homepage, name='homepage'),
    path('blog/', blog, name='blog'),
    path('maqola/<int:num>', maqola, name='maqola'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
