from django.conf.urls import url, include
from accounts import views
from accounts import url_reset


urlpatterns = [
    url(r'^logout$', views.logout, name="logout"),
    url(r'^login$', views.login, name="login"),
    url(r'^register$', views.registration, name="registration"),
    url(r'^profile$', views.user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
