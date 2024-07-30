# expenses/urls.py

from django.urls import path
from .views import ExpenseCreateView, UserExpensesView, AllExpensesView, DownloadBalanceSheetView

urlpatterns = [
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('user/<int:user_id>/', UserExpensesView.as_view(), name='user-expenses'),
    path('all/', AllExpensesView.as_view(), name='all-expenses'),
    path('download/', DownloadBalanceSheetView.as_view(), name='download-balance-sheet'),
]

