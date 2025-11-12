from django.urls import path
from accounts.apis import *

urlpatterns = [
    path('login/', login_view, name='login'),
]