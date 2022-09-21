from django.contrib import admin
from django.urls import path,include,re_path
admin.site.site_title= "Grand Hospital"
admin.site.site_header = "Grand Hospital"
admin.site.site_url = "Grand Hospital"
admin.site.index_title= "Dashboard"
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Grand Hospital API",
      default_version='v1',
      description="Grand Hospital",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="behzodtuit@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += i18n_patterns(
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path('api/v1/',include('doctors.urls')),
    path('api/v1/auth/',include('djoser.urls')),
    path('api/v1/auth/',include('djoser.urls.authtoken')),
    path('api/v1/',include('doctors.urls'))
                             )
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404 = 'doctors.views.error_404'