# api/urls.py
from django.urls import path
from . import views
from .views import EnqueteurListCreateAPIView, EnqueteListCreateAPIView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('', views.signin, name='home'),
path('enqueteurs/', EnqueteurListCreateAPIView.as_view(), name='enqueteur-list-create'),
    path('enquetes/', EnqueteListCreateAPIView.as_view(), name='enquete-list-create'),
]