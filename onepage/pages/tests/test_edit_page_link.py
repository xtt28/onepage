from django.test import TestCase
from users.models import AppUser
from pages.models import Page, PageLink


class PageLinkTestCase(TestCase):
    PATH = "/edit/links"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user")
        test_user.set_password("test_pass")
        test_user.save()
        Page.objects.create(user=test_user, description="Test page for links")

    def test_handles_unauthenticated_user(self):
        """A request to create a link by an authenticated user should redirect
        to the signin page."""
        response = self.client.get(self.PATH)
        self.assertNotEqual(200, response.status_code)

    def test_valid_changes_record_values(self):
        """A POST request with valid form values for a social profile should
        result in a record change."""
        self.client.login(username="test_user", password="test_pass")
        response = self.client.post(
            self.PATH, {"platform": "github", "value": "xtt28"}, follow=True
        )
        self.assertEqual(200, response.status_code)

        link = PageLink.objects.filter(page__user__username="test_user").first()
        self.assertIsNotNone(link)
        self.assertEqual(link.get_profile_link(), "https://github.com/xtt28")

    def test_urlencodes_changes_record_values(self):
        """A POST request with values that need to be URL encoded are URL
        encoded when accessed."""
        self.client.login(username="test_user", password="test_pass")
        response = self.client.post(
            self.PATH,
            {"platform": "github", "value": "xtt28/repositories"},
            follow=True,
        )
        self.assertEqual(200, response.status_code)

        link = PageLink.objects.filter(page__user__username="test_user").first()
        self.assertIsNotNone(link)
        self.assertEqual(
            link.get_profile_link(), "https://github.com/xtt28%2Frepositories"
        )
