from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.task = Task.objects.create(name="Тестовая задача", opisanie="Описание")

        self.list_url = reverse('task-list')
        self.detail_url = reverse('task-detail', kwargs={'pk': self.task.pk})

    def test_unauthenticated_user_cannot_access(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_tasks_list(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_create_task(self):
        self.client.login(username='testuser', password='password123')
        data = {"name": "Новая задача", "opisanie": "Сделать ТЗ"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        self.client.login(username='testuser', password='password123')
        data = {"name": "Обновленное название", "stat": True}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.stat)

    def test_delete_task(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_filter_tasks(self):
        self.client.login(username='testuser', password='password123')
        Task.objects.create(name="Готово", stat=True)

        response = self.client.get(self.list_url, {'stat': 'false'})
        self.assertEqual(len(response.data['results']), 1)
