from django.urls import path
from .views import OutcomeView, OutcomeRUDView, OutcomesRView

app_name = "outcome"

urlpatterns = [
	path('outcome/<int:outcomeId>', OutcomeRUDView.as_view()),
	path('outcome/<int:user>', OutcomesRView.as_view()),
	path('outcome/', OutcomeView.as_view()),
]