from django.urls import path
from owner import views
urlpatterns=[
path("add",views.add_book,name="bookadd")
]