from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth.models import User


class DeleteUserCommandTest(TestCase):

    def setUp(self):
        User.objects.create(username="jhon")

    def test_command_output(self):
        out = StringIO()
        call_command('delete_users', 1, 2, stdout=out)
        user1 = out.getvalue()
        user2 = out.getvalue()

        self.assertIn('User "jhon (1)" deleted with success!\n', user1)
        self.assertIn('User with id 2 does not exist.\n', user2)