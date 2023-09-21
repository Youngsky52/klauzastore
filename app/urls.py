from django.urls import path

from account.views import signup, logout_u, login_u
from app.views import index, detail

urlpatterns = [
    path('', index, name="index"),
    path('info/<int:id>/', detail, name="detail"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_u, name="logout"),
    path('login/', login_u, name="login"),

]