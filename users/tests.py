from unittest import TestCase

from django.test import TestCase
from users.forms import RegistrationForm

class TestRegistrationForm(TestCase):

    def test_register_form_is_valid(self):
        form = RegistrationForm(data={
            'username': 'cos',
            'email': 'djwowo3@umk.pl',
            'password1': 'sdfeeeg123',
            'password2': 'sdfeeeg123',
            'first_name': 'lot',
            'last_name': 'tot'
        })


        self.assertTrue(form.is_valid())

    def test_register_form_is_no_valid(self):
        form = RegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)


    def test_register_form_email_not_valid(self):
        form = RegistrationForm(data={
            'username': 'cos',
            'email': 'djwowo3umk.pl',
            'password1': 'sdfeeeg123',
            'password2': 'sdfeeeg123',
            'first_name': 'lot',
            'last_name': 'tot'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_register_form_email_umk_not_valid(self):
        form = RegistrationForm(data={
            'username': 'cos',
            'email': 'djwowo3@gmail.pl',
            'password1': 'sdfeeeg123',
            'password2': 'sdfeeeg123',
            'first_name': 'lot',
            'last_name': 'tot'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1, form.errors)