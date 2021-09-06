
from django.contrib import admin
from django.urls import path, include
from .views import home, Registro
from django.contrib.auth.views import LogoutView, LoginView
from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('registro', Registro.as_view(), name="Registro" ),
    #path('accounts/login/', allauth.account.views.LoginView.as_view( template_name='login.html '), name='login' ),
    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout")
]
