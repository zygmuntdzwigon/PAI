from django.contrib.auth.mixins import UserPassesTestMixin

class UserIsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.author:
            return True
        return False

class UserIsDebtorOrCreditorMixin(UserPassesTestMixin):
    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.creditor or self.request.user == debt.debtor:
            return True
        return False