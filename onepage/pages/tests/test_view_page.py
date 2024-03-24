from django.test import TestCase
from users.models import AppUser
from pages.models import Page, PageLink


class ViewPageTestCase(TestCase):
    TEMPLATE_NAME = "pages/view_page.html"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user", password="Unused")
        test_page = Page.objects.create(
            user=test_user, description="This is a test page description"
        )
        PageLink.objects.create(page=test_page, platform="github", value="xtt28")

        AppUser.objects.create(username="test_user_2", password="Unused")

    def test_handles_nonexistent_user_page_request(self):
        """A request for the page of a nonexistent user should return a 404 and
        not use the view_page template."""
        response = self.client.get("/@nonexistent_user")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, self.TEMPLATE_NAME)

    def test_handles_nonexistent_page_existent_user(self):
        """A request for the page of a user who exists but has no page should
        return a new page."""
        response = self.client.get("/@test_user_2")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.TEMPLATE_NAME)
        self.assertIn("test_user_2", str(response.content))

    def test_renders_user_info(self):
        """A request for a user's profile page should render the stored
        information about them."""
        response = self.client.get("/@test_user")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.TEMPLATE_NAME)
        self.assertIn("test_user", str(response.content))
        self.assertIn("This is a test page description", str(response.content))
        self.assertIn("https://github.com/xtt28", str(response.content))
