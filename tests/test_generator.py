from django.apps import apps
from django.db import models
from django.test import TestCase
from django_queryset_erd import generate_erd_from_queryset


class TestModel(models.Model):
    name = models.CharField(max_length=100)
 
    objects = models.Manager()

    class Meta:
        app_label = 'tests'


class RelatedModel(models.Model):
    test_model = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    
    objects = models.Manager()

    class Meta:
        app_label = 'tests'


class ERDGeneratorTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        apps.get_app_config('tests').import_models()

    def test_generates_diagram_for_simple_queryset(self):
        queryset = TestModel.objects.all()
        diagram = generate_erd_from_queryset(queryset)

        self.assertIn('erDiagram', diagram)
        self.assertIn('TestModel', diagram)

    def test_includes_related_models(self):
        queryset = TestModel.objects.prefetch_related('relatedmodel_set')
        diagram = generate_erd_from_queryset(queryset)

        self.assertIn('TestModel', diagram)
        self.assertIn('RelatedModel', diagram)
        self.assertIn('RelatedModel ||--o{ TestModel', diagram)

    def test_diagram_content(self):
        queryset = TestModel.objects.all()
        diagram = generate_erd_from_queryset(queryset)
        expected_content = [
            'erDiagram',
            '{ TestModel',
        ]

        for content in expected_content:
            self.assertIn(content, diagram)
