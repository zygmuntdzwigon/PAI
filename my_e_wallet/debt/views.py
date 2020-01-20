from django.shortcuts import render
from django.http import HttpResponse
from .models import Debt, DebtStatuses
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
    )
from .mixins import UserIsAuthorMixin, UserIsDebtorOrCreditorMixin
from .forms import DebtForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'debt/home.html')

def about(request):
    return render(request, 'debt/about.html')

def markaspaid(request, pk):
    debt = Debt.objects.filter(id=pk).first()
    debt.status = DebtStatuses.objects.filter(status="Paid").first()
    debt.save()
    return HttpResponse()

def not_found(request, exception):
    return render(request, 'debt/404.html')

class DebtListView(LoginRequiredMixin, ListView):
    model = Debt
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['ascreditor'] = Debt.objects.filter(creditor=self.request.user)
        context_data['asdebtor'] = as_debtor = Debt.objects.filter(debtor=self.request.user)
        return context_data
 

class DebtDetailView(LoginRequiredMixin, UserIsDebtorOrCreditorMixin, DetailView):
    model = Debt


class DebtCreateView(LoginRequiredMixin, CreateView):
    model = Debt
    form_class = DebtForm

    def form_valid(self, form):
        form.instance.status = DebtStatuses.objects.filter(status='Pending').first()
        debtor = form.instance.debtor
        creditor = form.instance.creditor
        author = self.request.user
        form.instance.author = author
        errors = []
        if debtor == creditor:
            errors.append("Creditor and debtor cannot be the same users")
        
        if author != debtor and author != creditor:
            errors.append("You must be eighter creditor or debtor")
        if errors:
            raise ValidationError(errors)
        
        return super().form_valid(form) 


class DebtDeleteView(LoginRequiredMixin, UserIsAuthorMixin, DeleteView):
    model = Debt
    success_url = '/debts'


class DebtUpdateView(LoginRequiredMixin, UserIsDebtorOrCreditorMixin, UpdateView):
    model = Debt
    template_name = 'debt/debt_update.html'
    form_class = DebtForm

    def form_valid(self, form):
        form.instance.status = DebtStatuses.objects.filter(status='Pending').first()
        form.instance.author = self.request.user
        return super().form_valid(form)
