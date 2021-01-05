from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()

        # define the values which should be entered in the db
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'password'
        )

        # check if values are stored correctly in the db
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)

        self.assertEqual(str(super_user), 'testuser@super.com')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'testuser@super.com', 'password', is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'testuser@super.com', 'password', is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                '', 'password'
            )


    def test_new_user(self):
        db = get_user_model()

        # define the values which should be entered in the db
        user = db.objects.create_user(
            'testuser@normal.com', 'password'
        )

        # check if values are stored correctly in the db
        self.assertEqual(user.email, 'testuser@normal.com')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                '', 'password'
            )
