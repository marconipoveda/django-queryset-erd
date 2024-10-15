from django.db.models import ForeignKey, ManyToManyField
from django.db.models.fields.reverse_related import ForeignObjectRel


def generate_erd_from_queryset(queryset) -> str:
    """
    Generate a Mermaid ERD diagram from a Django queryset

    Args:
        queryset: A Django QuerySet object

    Returns:
        str: A string containing the Mermaid diagram code

    Example:
        from myapp.models import MyModel
        from django_queryset_erd import generate_erd_from_queryset

        queryset = MyModel.objects.select_related('related_model')
        diagram = generate_erd_from_queryset(queryset)
        print(diagram)
    """
    main_model = queryset.model

    processed_models = set()
    relationships = set()

    def process_model(model):
        if model in processed_models:
            return

        processed_models.add(model)

        # Process all fields in the model
        for field in model._meta.get_fields():
            # Handle foreign keys
            if isinstance(field, ForeignKey):
                related_model = field.related_model
                relationships.add((model.__name__, related_model.__name__, field.name, '||--o{'))
                process_model(related_model)

            # Handle many-to-many relationships
            elif isinstance(field, ManyToManyField):
                related_model = field.related_model
                relationships.add((model.__name__, related_model.__name__, field.name, '}o--o{'))
                process_model(related_model)

            # Handle reverse relationships
            elif isinstance(field, ForeignObjectRel):
                related_model = field.related_model
                # Only process if it's pointing back to us
                if related_model == model:
                    continue
                relationships.add((related_model.__name__, model.__name__, field.name, '||--o{'))
                process_model(related_model)

    process_model(main_model)

    mermaid_code = ["erDiagram"]
    for rel in relationships:
        model1, model2, field_name, relation_type = rel
        mermaid_code.append(f"    {model1} {relation_type} {model2} : {field_name}")

    return "\n".join(mermaid_code)

