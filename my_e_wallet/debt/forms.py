from django.forms import ModelForm, ValidationError
from .models import Debt

class DebtForm(ModelForm):
    class Meta:
        model = Debt
        fields = [
            'title',
            'description',
            'amount',
            'category',
            'creditor',
            'debtor',
        ]

