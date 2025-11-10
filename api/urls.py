from django.urls import path
from api.apis import *

urlpatterns = [
    path('hello/', hello),
]
