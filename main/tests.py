import uuid
from django.test import TestCase, Client
from django.urls import reverse
from main.models import Experience, Project


class ExperienceViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('main:show_experience')

    def test_url_accessible_and_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience.html')

    def test_data_appears_when_exists(self):
        Experience.objects.create(
            title="Test Experience",
            description="Deskripsi test experience",
            category="internship",
        )
        response = self.client.get(self.url)
        self.assertContains(response, "Test Experience")

    def test_empty_state_when_no_data(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")


class ProjectViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('main:show_projects')

    def test_url_accessible_and_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

    def test_data_appears_when_exists(self):
        Project.objects.create(
            title="Test Project",
            description="Deskripsi test project",
            category="personal",
        )
        response = self.client.get(self.url)
        self.assertContains(response, "Test Project")

    def test_empty_state_when_no_data(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Belum ada proyek yang ditambahkan.")