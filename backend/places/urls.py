from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.getAll, name="all"),
    path('route', views.getRoute, name="route"),
    # path('sendroute', views.sendRoute, name="sendroute"),
    path('refresh/<int:image_id>/', views.changeOption, name="refresh"),
    path('weather',views.getWeather,name="weather")
]
