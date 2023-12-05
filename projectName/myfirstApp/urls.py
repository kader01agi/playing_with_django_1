from django.urls import path
from . import views

urlpatterns = [
    path('',views.apps_first_resp, name="first_app_home"),
    path('form/',views.templating)
]
