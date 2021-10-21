from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests (TestCase):
    
    def test_create_user_with_email_successful(self):

        """ Test creating a new user with an email is successful """
        email = 'test.email@test.com'
        password = 'Test.password'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):

        """ test the email for a new user is normalized """
        email = 'test@TEST.DOMAIN.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEquals(user.email, email.lower())


    def test_new_user_invalid_email(self):

        """ test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
