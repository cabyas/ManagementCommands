from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays the text "Hello world"'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='a name to greet him')
        parser.add_argument('--foo', action='store_const', const=42)

    def handle(self, *args, **kwargs):
        """
        Prints "hello <name value>" or "hello world" if any name is provided a "42"
        in a new line if the argument "--foo" is passed.

        Expected results:
        > python manage.py hello_args --name John
        hello John
        None

        > python manage.py hello_args --name John --foo
        hello John
        42

        > python manage.py hello_args --foo
        hello None
        42
        """
        # we can use this approach to give a default value to a param
        # but is recommended used (for this particular case) "store_str"
        # instead
        #
        # Note: kwargs.get('name', 'world') won't work as you could expect
        # because the key 'name' exist but has as value None
        name = kwargs.get('name') or 'world'
        self.stdout.write(f'hello {name}')

        a = kwargs.get('foo')
        self.stdout.write(f'{a}')