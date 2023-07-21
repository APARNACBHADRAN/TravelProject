from. import views
from django.urls import path

urlpatterns = [

    # path('',views.demo,name='demo'),
    path('',views.first,name='first'),
path('result/',views.addition,name='add')
]