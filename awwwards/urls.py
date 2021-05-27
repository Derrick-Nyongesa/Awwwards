from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homePage'),
    #path('api/awwwards/', views.ProfileList.as_view()),
    path('api/awwwards/', views.ProjectsList.as_view()),
    path('profile/<username>/', views.profile, name='profile'),
    #path('project/<projects>', views.single_project, name='project'),
    
]