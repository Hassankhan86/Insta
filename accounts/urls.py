from django.urls import path, include
from .import views
app_name = 'accounts'


urlpatterns = [
    path('addaccount', views.createAccount, name='addaccount'),
    path('accountview', views.accountview, name='accountview'),
    path('update_account/<id>/', views.updateaccount, name="updateaccount"),
    path('delete_account/<id>/', views.deleteaccount, name='deleteaccount'),
    path('home/', views.home, name='abc'),
    path('comments', views.commentview,  name='commentview'),
    path('addcomment', views.addcomment, name='addcomment'),
    path('update_comment/<id>/', views.updatecomment, name="updatecomment"),
    path('delete_comment/<id>/', views.deletecomment, name='deletecomment'),

    path('instabotcode', views.instabotcode, name='instabotcode'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('report/', views.reportview, name='report'),
    path('error_message/', views.errormessage, name='ErrorMessage'),

]