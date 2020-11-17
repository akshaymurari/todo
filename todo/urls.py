from django.urls import path
from . import views
urlpatterns=[
    path('',views.fun,name="fun"),
    path('add',views.add,name="add"),
    path('dell',views.dell,name="dell"),
    path('edit',views.edit,name="edit"),
]