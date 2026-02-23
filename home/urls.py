from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(),name='login'),
    path('logout', views.LogoutInterfaceView.as_view(),name='logout'),
    path('register', views.RegisterView.as_view(),name='register'),
    path('password-reset', views.PasswordResetInterfaceView.as_view(),name='password-reset'),
    path('password-reset/done',views.PasswordResetDoneInterfaceView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', views.PasswordResetConfirmInterfaceView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',views.PasswordResetCompleteInterfaceView.as_view(),name='password_reset_complete'),
]