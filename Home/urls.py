from django.conf.urls import url
from.import views

app_name = 'Home'

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^signup/', views.UserFormView.as_view(), name='signup'),
    url(r'^login/', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^boards/', views.board, name='boards'),
]