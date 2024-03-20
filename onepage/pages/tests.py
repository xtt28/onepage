from django.test import TestCase
from users.models import AppUser
from .models import Page


class ViewPageTestCase(TestCase):
    TEMPLATE_NAME="pages/view_page.html"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user", password="Unused")
        Page.objects.create(
            user=test_user, description="This is a test page description"
        )

    def test_handles_nonexistent_page_request(self):
        """A request for the page of a nonexistent user should return a 404 and
        not use the view_page template."""
        response = self.client.get("/@nonexistent_user")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, self.TEMPLATE_NAME)

    def test_renders_user_info(self):
        """A request for a user's profile page renders the stored information
        about them."""
        response = self.client.get("/@test_user")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.TEMPLATE_NAME)
        self.assertIn("test_user", str(response.content))
        self.assertIn("This is a test page description", str(response.content))
