from django.urls import path
from .import views

app_name='blogapp'

urlpatterns=[
    path('',views.BlogListView.as_view(),name='list'),
    path('<int:pk>/',views.BlogDetailView.as_view(),name='detail'),
    path('createaccount/',views.createaccount,name='createaccount'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('createpost/',views.createpost,name='createpost'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profiles/',views.profiles,name='profiles'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('update/<int:pk>/',views.BlogUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.BlogDeleteView.as_view(),name='delete')
]