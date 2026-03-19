from django.contrib import admin
from django.urls import path
from posts.views import home_view, post_detail 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "لوحة التحكم"
admin.site.site_title = "قرطاس"
admin.site.index_title = "مرحبا بك في لوحة التحكم"