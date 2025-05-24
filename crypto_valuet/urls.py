from django.urls import path
from.import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('classs', views.classs, name='classs'),
    path('single_1/<int:idd>',views.single_1, name='single_1'),
    path('single_2/<int:idd>',views.single_2, name='single_2'),
    path('single_3/<int:idd>',views.single_3, name='single_3'),
    path('add-product/', views.add_product, name='add_product')
]

