from django.urls import path
from .views import UserView, UserRUDView

app_name = "user"

urlpatterns = [
	path('user/<str:email>', UserRUDView.as_view()),
	path('user/', UserView.as_view()),
]