from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='derrick', password='E)a7vzB9')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='derrick')
        self.project = Projects.objects.create(id=1, title='test post', photo='https://images.pexels.com/photos/1974385/pexels-photo-1974385.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260', description='test description',
                                        user=self.user, url='https://www.pexels.com/photo/grayscale-photo-of-a-woman-in-a-garden-1974385/')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

    def test_save_projects(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_projects(self):
        self.project.save()
        projects = Projects.all_projects()
        self.assertTrue(len(projects) > 0)

    def test_search_project(self):
        self.project.save()
        project = Projects.search_project('test')
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = Projects.search_project('test')
        self.assertTrue(len(project) < 1)
