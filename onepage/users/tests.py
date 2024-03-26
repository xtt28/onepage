from django.contrib.auth import get_user
from django.test import TestCase
from users.models import AppUser
from pages.models import Page, PageLink


class UserDeleteTestCase(TestCase):
    PATH = "/you/delete/final"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user")
        test_user.set_password("test_pass")
        test_user.save()
        Page.objects.create(
            user=test_user, description="This is a test page description"
        )

    def test_handles_unauthenticated_user(self):
        """A request to delete a user by an unauthenticated user should not
        succeed."""
        response = self.client.get(self.PATH)
        self.assertNotEqual(200, response.status_code)
        self.assertEqual(AppUser.objects.count(), 1)
        self.assertEqual(Page.objects.count(), 1)

    def test_deletes_user(self):
        """A request to delete a user by an authenticated user should delete the
        user's account."""
        self.client.login(username="test_user", password="test_pass")
        response = self.client.get(self.PATH)
        self.assertEqual(AppUser.objects.count(), 0)
        self.assertEqual(Page.objects.count(), 0)


class UserLogoutTestCase(TestCase):
    PATH = "/you/logout"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user")
        test_user.set_password("test_pass")
        test_user.save()

    def test_handles_unauthenticated_user(self):
        """A request to log out by an unauthenticated user should not succed."""
        response = self.client.get(self.PATH)
        self.assertNotEqual(200, response.status_code)

    def test_logs_out(self):
        """A request to log out by an authenticated user should log the user
        out."""
        self.client.login(username="test_user", password="test_pass")
        self.client.get(self.PATH)

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
