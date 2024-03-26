from django.test import TestCase
from users.models import AppUser
from pages.models import Page, PageLink


class PageLinkTestCase(TestCase):
    PATH = "/edit/links"
    DELETE_PATH = PATH + "/delete/"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user")
        test_user.set_password("test_pass")
        test_user.save()
        test_user_2 = AppUser.objects.create(username="test_user_2")
        test_user_2.set_password("test_pass")
        test_user_2.save()

        self.test_page = Page.objects.create(
            user=test_user, description="Test page for links"
        )

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

    def test_deletes_link(self):
        """A DELETE request to delete a link on the user's page should delete the
        link."""
        self.client.login(username="test_user", password="test_pass")
        PageLink.objects.create(pk=1, page=self.test_page)
        response = self.client.delete(self.DELETE_PATH + "1")
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, PageLink.objects.filter(pk=1).count())

    def test_not_deletes_other_user_link(self):
        """A DELETE request to delete a link on another user's page should not
        delete the link."""
        self.client.login(username="test_user_2", password="test_pass")
        PageLink.objects.create(pk=1, page=self.test_page)
        response = self.client.delete(self.DELETE_PATH + "1")
        self.assertNotEqual(200, response.status_code)
        self.assertEqual(1, PageLink.objects.filter(pk=1).count())

    def test_not_deletes_link_unauthenticated(self):
        """A DELETE request to delete any link should fail if the user is not
        authenticated."""
        PageLink.objects.create(pk=1, page=self.test_page)
        response = self.client.delete(self.DELETE_PATH + "1")
        self.assertNotEqual(200, response.status_code)
        self.assertEqual(1, PageLink.objects.filter(pk=1).count())
