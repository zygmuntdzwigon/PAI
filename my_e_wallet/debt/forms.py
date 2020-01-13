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

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        debtor = cleaned_data.get('debtor')
        creditor = cleaned_data.get('creditor')
        errors = []
        if debtor == creditor:
            errors.append("Creditor and debtor cannot be the same users")
        
        if debtor != author and creditor != author:
            errors.append("You must be eighter creditor or debtor")

        if errors:
            raise ValidationError(errors)

    def form_valid(self, form):
        form.instance.status = DebtStatuses.objects.filter(status='Pending').first()
        form.instance.author = self.request.user
        return super().form_valid(form) 
