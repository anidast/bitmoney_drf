from django.urls import path
from .views import UserView, UserRUDView, LoginView

app_name = "user"

urlpatterns = [
	path('user/<int:userId>', UserRUDView.as_view()),
	path('user/', UserView.as_view()),
	path('login/', LoginView.as_view()),
]