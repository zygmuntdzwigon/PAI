from django.contrib import admin
from .models import DebtStatuses, DebtCategories, Debt

# Register your models here.
admin.site.register(DebtStatuses)
admin.site.register(DebtCategories)
admin.site.register(Debt)