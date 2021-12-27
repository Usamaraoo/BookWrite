from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# Local imports
from apies.views import IndexApi
# 3rd party
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apies.urls')),
    path('', IndexApi.as_view()),
    # token auth
    path('user-token/', views.obtain_auth_token),

]
