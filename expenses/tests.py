import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Expense
from users.models import User
from unittest.mock import patch

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user():
    return User.objects.create(username='testuser', password='testpass')

@pytest.fixture
def test_expense(test_user):
    return Expense.objects.create(
        user=test_user,
        description='Test Expense',
        amount=100,
        split_type='equal',
        split_details='[{"user": "testuser", "amount": 100}]'
    )

def test_create_expense(api_client, test_user):
    url = reverse('expense-create')
    data = {
        "user": test_user.id,
        "description": "Dinner",
        "amount": 50,
        "split_type": "equal",
        "split_details": [{"user": "testuser", "amount": 50}]
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

def test_user_expenses(api_client, test_user, test_expense):
    url = reverse('user-expenses', kwargs={'user_id': test_user.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['description'] == 'Test Expense'

def test_all_expenses(api_client, test_expense):
    url = reverse('all-expenses')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['description'] == 'Test Expense'

@patch('expenses.views.csv.writer')
def test_download_balance_sheet(mock_csv_writer, api_client):
    url = reverse('download-balance-sheet')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response['Content-Type'] == 'text/csv'
    assert response['Content-Disposition'] == 'attachment; filename="balance_sheet.csv"'
    mock_csv_writer.assert_called_once()  # Ensures the CSV writer was called
