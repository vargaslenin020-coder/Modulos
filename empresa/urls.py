from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # SOLO UNA de estas líneas - ELIMINA LA OTRA
    path('accounts/', include('django.contrib.auth.urls')),
    
    # ELIMINA esta línea duplicada:
    # path('cuentas/', include('django.contrib.auth.urls')),
    
    path('accounts/profile/', views.perfil, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('modulos/', views.modulos, name='modulos'),
    path('modulo1/', views.modulo1, name='modulo1'),
    path('modulo2/', views.modulo2, name='modulo2'),
    path('modulo3/', views.modulo3, name='modulo3'),
    path('modulo4/', views.modulo4, name='modulo4'),
    path('modulo5/', views.modulo5, name='modulo5'),
    path('modulo6/', views.modulo6, name='modulo6'),
    path('modulo7/', views.modulo7, name='modulo7'),
    
    # URLs de recuperación de contraseña
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt',
             success_url='/password-reset/done/'
         ), 
         name='password_reset'),
    
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             success_url='/password-reset-complete/'
         ), 
         name='password_reset_confirm'),
    
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]