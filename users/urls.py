from django.urls import path
from .views import * # * memanggil semua fungsi yang ada didalam file views

urlpatterns = [
	path('', list_users,name='list_users'),
]