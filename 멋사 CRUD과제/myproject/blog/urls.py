from django.urls import path
from . import views  #urls와 같은레벨에 있는 현재 폴더에서 VIEWS를 가져오는 것임 

urlpatterns = [
    path('<int:blog_id>' , views.detail, name ='detail'),   #원래 views의 앱네임이 있던 상태에서 지운것임 
    path('new/', views.new , name='new'),
    path('create/', views.create , name='create'),
    path('<int:blog_id>/delete/' , views.delete, name='delete'),
    path('<int:blog_id>/update/' , views.update, name='update'),
    path('simple/' , views.simple, name='simple'),
    path('fake/',views.fake, name='fake'),
]