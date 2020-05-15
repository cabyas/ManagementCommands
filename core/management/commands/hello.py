from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays the text "Hello world"'

    def handle(self, *args, **kwargs):
        self.stdout.write('hello world')