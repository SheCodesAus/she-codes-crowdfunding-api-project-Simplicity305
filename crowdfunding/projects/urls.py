from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail")

]
urlpatterns = format_suffix_patterns(urlpatterns) #something that gets included in the django rest framework so not sure if need 
#ths is a function which takes all your urls and tells it whether you want json or something else back??? Value of it is low 
