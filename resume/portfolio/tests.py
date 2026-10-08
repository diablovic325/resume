from django.test import TestCase
from django.urls import reverse


class PortfolioPageTests(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_returns_200(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_skills_page_returns_200(self):
        response = self.client.get(reverse('skills'))
        self.assertEqual(response.status_code, 200)
