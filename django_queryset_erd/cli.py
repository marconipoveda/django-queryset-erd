import argparse
import django
from django.apps import apps

from .generator import generate_erd_from_queryset


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('app_label', help='Django application label')
    parser.add_argument('model_name', help='Model name')
    args = parser.parse_args()

    django.setup()
    model = apps.get_model(args.app_label, args.model_name)
    queryset = model.objects.all()

    print(generate_erd_from_queryset(queryset))


if __name__ == '__main__':
    main()

