from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name = 'index'),
    path("sign-up/", views.SignUpView, name = 'sign-up'),
    path("sign-in/", views.SignInView, name = 'sign-in'),
    path("sign-out/", views.SignOutView, name = 'sign-out'),
    path("deleteUSerstemplate/", views.deleteUserstemplate, name = 'deleteUserstemplate'),
    path("deleteUSers/", views.deleteUsers, name = 'deleteUSers'),
    path("viewUsersList/", views.viewUsersList, name = 'viewUsersList'),
    path('deleteByUserName/<int:pk>', views.deleteByUserName, name='deleteByUserName'),
    path('search/', views.search, name='search'),    
    path('searchByUserNameFilter/', views.searchByUserNameFilter, name='searchByUserNameFilter'),   
    path('query/', views.query,name="query_results"),
]
