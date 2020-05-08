from django.urls import path
from .views import UserView, UserRUDView

app_name = "user"

urlpatterns = [
	path('user/<int:userId>', UserRUDView.as_view()),
	path('user/', UserView.as_view()),
]