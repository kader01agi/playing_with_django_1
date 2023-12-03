from django.urls import path
from . import views

urlpatterns = [
    path('',views.apps_first_resp),
    path('form/',views.templating)
]
