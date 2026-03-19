import unittest
from flask import Flask, request
import app

class TestTaskAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.app
        self.client = self.app.test_client()

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)

    def test_get_task(self):
        # Create a task first
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post('/tasks', data=request.json_encode(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        task_id = response.json['id']

        response = self.client.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], task_id)

    def test_create_task(self):
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post('/tasks', data=request.json_encode(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], 'Test Task')

    def test_update_task(self):
        # Create a task first
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post('/tasks', data=request.json_encode(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        task_id = response.json['id']

        # Update the task
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(f'/tasks/{task_id}', data=request.json_encode(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Updated Task')

    def test_delete_task(self):
        # Create a task first
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post('/tasks', data=request.json_encode(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        task_id = response.json['id']

        # Delete the task
        response = self.client.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'ok')

if __name__ == '__main__':
    unittest.main()