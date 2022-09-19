from django.contrib import admin
from django.urls import path,include
admin.site.site_title= "Grand Hospital"
admin.site.site_header = "Grand Hospital"
admin.site.site_url = "Grand Hospital"
admin.site.index_title= "Dashboard"
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path('api/v1/',include('doctors.urls')),
    path('api/v1/auth/',include('djoser.urls')),
    path('api/v1/auth/',include('djoser.urls.authtoken')),
    path('api/v1/',include('doctors.urls'))
                             )
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404 = 'doctors.views.error_404'