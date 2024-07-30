from rest_framework import generics, status
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from django.http import HttpResponse, JsonResponse
import csv

class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserExpensesView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Expense.objects.filter(user_id=user_id)

class AllExpensesView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class DownloadBalanceSheetView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            expenses = Expense.objects.all()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'

            writer = csv.writer(response)
            writer.writerow(['User', 'Description', 'Amount', 'Split Type', 'Split Details'])
            for expense in expenses:
                writer.writerow([expense.user.email, expense.description, expense.amount, expense.split_type, expense.split_details])
            return response
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while generating the balance sheet'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
