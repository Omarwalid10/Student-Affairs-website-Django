from . import views
from django.urls import path

urlpatterns = [
    path('',views.BeginHomepage,name="beginhomepage"),
    path('homepage',views.homepage,name="homepage"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('edit',views.edit,name="edit"),
    path('<str:SearchedName>/assignment',views.assignment,name="assignment"),
    path('search',views.search, name="search"),
    path('studentlist',views.studentlist,name="studentlist"),
    path('<str:std_ID>/update',views.update,name="update"),
    path('<str:std_ID>/delete',views.delete,name="delete"),
    path('<str:std_ID>/editing',views.editing,name="editing")
]
