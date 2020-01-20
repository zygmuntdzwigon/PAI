from django.urls import path
from .views import (
    DebtListView,
    DebtDetailView,
    DebtCreateView,
    DebtUpdateView,
    DebtDeleteView,
    )
from . import views

urlpatterns = [
    path('', views.home, name='debt-home'),
    path('about/', views.about, name='debt-about'),
    path('debts/', DebtListView.as_view(), name='debts'),
    path('debts/<int:pk>/', DebtDetailView.as_view(), name='debt-detail'),
    path('debts/<int:pk>/update/', DebtUpdateView.as_view(), name='debt-update'),
    path('debts/<int:pk>/delete/', DebtDeleteView.as_view(), name='debt-delete'),
    path('debts/new/', DebtCreateView.as_view(), name='debt-create'),
    path('debts/<int:pk>/paid', views.markaspaid, name='debt-paid')
]


handler404 = 'debt.views.not_found'