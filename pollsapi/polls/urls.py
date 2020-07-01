from django.urls import path
from . import views
from .views import polls_detail,polls_list

urlpatterns=[
    path('polls/',views.polls_list,name="polls_list"),
    path('polls/<int:pk>/',views.polls_detail,name="polls_detail")
]