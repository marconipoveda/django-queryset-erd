from django.test import TestCase
from django.db import models
from django_queryset_erd import generate_erd_from_queryset

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'test_app'

class RelatedModel(models.Model):
    test_model = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'test_app'

class ERDGeneratorTests(TestCase):
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
