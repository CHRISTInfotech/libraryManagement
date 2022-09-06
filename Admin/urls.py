from django.urls import path

from Admin.views import head


urlpatterns = [
    path('head', head, name="head")
]
