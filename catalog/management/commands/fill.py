from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'A'},
            {'name': 'B'},
            {'name': 'C'}
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
