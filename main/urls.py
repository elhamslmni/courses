from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('login', views.login_page, name="login_page"),
    path('register', views.register_page, name="register_page"),
    path('logout', views.log_out, name="log_out"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('profile', views.profile, name="profile"),
    path('setting_page', views.setting_page, name="setting_page"),
    path('panel', views.panel, name="panel"),
    path('make_new_course', views.make_new_course, name="make_new_course"),
    path('all_course', views.courses, name="courses"),
    path('search', views.search, name="search"),
]
