from django.test import TestCase


from todo.models import TodoList

class TodolistModelTest(TestCase):
	@classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        TodoList.objects.create(title='Начать бегать', created='25.12.2019', due_date='28.12.2019')

    def test_title_label(self):
        title=TodoList.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

# Create your tests here.
