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


# Create your views here.
def home(request):
    return render(request, 'debt/home.html')

def about(request):
    return render(request, 'debt/about.html')


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
