from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class DebtCategories(models.Model):
    category = models.CharField(max_length=50, default="debt category")

    def __str__(self):
        return self.category

class DebtStatuses(models.Model):
    status = models.CharField(max_length=50, default="debt status")

    def __str__(self):
        return self.status

class Debt(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    category = models.ForeignKey(DebtCategories, on_delete=models.DO_NOTHING, default=1)
    status = models.ForeignKey(DebtStatuses, on_delete=models.DO_NOTHING, default=1)
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myDebts")
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="debtors", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('debt-detail', kwargs={'pk': self.pk})


