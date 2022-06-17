from django.contrib import admin
from django.urls import path, include
from Home.views import home, register_request, login_request, logout_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path('products/', include('Products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
