from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path("", views.index, name='home'),
    path("coffee/", views.coffee_view, name = 'coffee'),
    path("coffee/<int:question_id>/", views.detail, name = 'detail'),
    path("describe/", views.describe, name = 'describe'),
    ]
