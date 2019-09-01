from django.urls import path
from . import views
"""현재 위치에서 views를 import해 와서 쓴다"""
"""admin 관련된 애는 admin.site에 있는 url을 사용하겠다"""
"""fcuser로 관련되어 요청이 오는 애는  fcuser 아래에 있는 url을 사용하겠다"""

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('home/', views.home)
]
