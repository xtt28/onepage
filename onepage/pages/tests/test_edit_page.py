from django.test import TestCase
from users.models import AppUser
from pages.models import Page, PageLink


class EditPageTestCase(TestCase):
    TEMPLATE_NAME = "pages/edit_page.html"
    PATH = "/edit"

    def setUp(self):
        test_user = AppUser.objects.create(username="test_user")
        test_user.set_password("test_pass")
        test_user.save()
        Page.objects.create(
            user=test_user, description="This is a test page description"
        )

    def test_handles_unauthenticated_user(self):
        """A request to edit a page by an authenticated user should redirect to
        the signin page."""
        response = self.client.get(self.PATH)
        self.assertNotEqual(200, response.status_code)
        self.assertTemplateNotUsed(response, self.TEMPLATE_NAME)

    def test_renders_edit_view(self):
        """A GET request to edit a page by an authenticated user should render
        a template with a form."""
        self.client.login(username="test_user", password="test_pass")
        response = self.client.get(self.PATH)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.TEMPLATE_NAME)
        self.assertIn("This is a test page description", str(response.content))

    def test_changes_record_values(self):
        """A POST request with valid form values should update the record data."""
        self.client.login(username="test_user", password="test_pass")
        response = self.client.post(
            self.PATH, {"description": "Updated description"}, follow=True
        )
        self.assertRedirects(response, "/@test_user")
        self.assertIn("Updated description", str(response.content))
        self.assertNotIn("This is a test page description", str(response.content))
