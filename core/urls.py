from django.urls import path, include
from django.contrib.auth import views as Auth_Views
from .views import IndexView, LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('logout/', Auth_Views.LogoutView.as_view(), name='logout'),

]