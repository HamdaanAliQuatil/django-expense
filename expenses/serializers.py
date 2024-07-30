from rest_framework import serializers
from .models import Expense
from django.core.exceptions import ValidationError

class ExpenseSerializer(serializers.ModelSerializer):
    split_details = serializers.JSONField()

    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'split_type', 'split_details', 'created_at']

    def validate_split_details(self, value):
        split_type = self.initial_data.get('split_type')
        if split_type == 'percentage':
            total_percentage = sum(item['percentage'] for item in value)
            if total_percentage != 100:
                raise serializers.ValidationError("Total percentage must add up to 100.")
        elif split_type == 'exact':
            total_amount = sum(item['amount'] for item in value)
            if total_amount != float(self.initial_data.get('amount')):
                raise serializers.ValidationError("Total amounts in split details must equal the expense amount.")
        return value
