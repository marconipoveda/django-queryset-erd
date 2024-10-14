# Django Queryset ERD Generator

Generate Entity-Relationship Diagrams from Django querysets using Mermaid notation.

## Installation

```bash
pip install django-queryset-erd
```

## Usage

```python
from your_app.models import YourModel
from django_queryset_erd import generate_erd_from_queryset

queryset = YourModel.objects.select_related('related_model')
diagram = generate_erd_from_queryset(queryset)
print(diagram)
```

## Features

- Generates Mermaid ERD diagrams from Django querysets
- Supports ForeignKey and ManyToManyField relationships
- Handles reverse relationships

## Requirements

- Python 3.12+
- Django >= 4.2

## License

This project is licensed under the MIT License - see the LICENSE file for details.
