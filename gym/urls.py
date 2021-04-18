""" GYM URL Configuration """

# Django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# Views
from users import views as user_views

# Decorators
from users.decorators import unauthenticated_user

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='payment/index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('payment/', include('payment.urls')),
    path('login/', unauthenticated_user(auth_views.LoginView.as_view(
        template_name='users/login.html')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)