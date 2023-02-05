from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('events/register/<event_id>', views.register, name='event-register'),
    path('events/unregister/<event_id>', views.unregister, name='event-unregister'),
    path('about/', views.about, name='about'),
    path('conferences/', views.conferences, name='conferences'),
    path('paperpresentations/', views.paper_presentations, name='paper-presentations'),
    path('virtualtour/', views.virtual_tour, name='virtual-tour'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('reset_password/',
    #  auth_views.PasswordResetView.as_view(template_name="pages/password_reset.html"),
    #  name="reset_password"),

    # path('reset_password_sent/', 
    #     auth_views.PasswordResetDoneView.as_view(template_name="pages/password_reset_sent.html"), 
    #     name="password_reset_done"),

    # path('reset/<uidb64>/<token>/',
    #  auth_views.PasswordResetConfirmView.as_view(template_name="pages/password_reset_form.html"), 
    #  name="password_reset_confirm"),

    # path('reset_password_complete/', 
    #     auth_views.PasswordResetCompleteView.as_view(template_name="pages/password_reset_done.html"), 
    #     name="password_reset_complete"),
]
