from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('tasks.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
