from django.urls import path

from . import views

app_name = "comic"

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:detail_id>', views.detail_view, name='detail_view'),
]