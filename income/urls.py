from django.urls import path
from .views import IncomeView, IncomeRUDView, IncomesRView

app_name = "income"

urlpatterns = [
	path('income/<int:incomeId>', IncomeRUDView.as_view()),
	path('incomes/<int:user>', IncomesRView.as_view()),
	path('income/', IncomeView.as_view()),
]