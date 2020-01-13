from django.contrib.auth.mixins import UserPassesTestMixin

class UserIsModeratorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.profile.is_moderator