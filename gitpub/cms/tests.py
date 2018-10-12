from django.test import TestCase, TransactionTestCase 
from cms.models import AnonymousUser, Student, Admin
from django.db import transaction

# Create your tests here.
class UserCreationTestCase(TransactionTestCase):
    # Anonymous User
    def test_anonymous_user_creation(self):
        quantity = len(AnonymousUser.objects.all())

        AnonymousUser.objects.create(name="Any name")

        self.assertEqual(len(AnonymousUser.objects.all()), quantity + 1)

    def test_anonymous_user_is_singleton(self):
        quantity = len(AnonymousUser.objects.all())

        first_anonymous_user = AnonymousUser.objects.create(name="Any name")
        second_anonymous_user = AnonymousUser.objects.create(name="Any name")

        self.assertEqual(len(AnonymousUser.objects.all()), quantity + 1)
        self.assertEqual(first_anonymous_user, second_anonymous_user)

    def test_anonymous_user_default_name(self):
        anonymous_user = AnonymousUser.objects.create()
        self.assertEqual(anonymous_user.name, "Anonymous User")

        anonymous_user2 = AnonymousUser.objects.create(name="Any name")
        self.assertEqual(anonymous_user2.name, "Anonymous User")

    # Student
    def test_student_creation(self):
        quantity = len(Student.objects.all())
        Student.objects.create(
            name="Any name",
            registry="0000000",
            email="student@email.com",
            password="pwd123"
            )

        self.assertEqual(len(Student.objects.all()), quantity + 1)

    def test_student_duplicate_email(self):
        quantity = len(Student.objects.all())
        Student.objects.create(
            name="Any name",
            registry="0000000",
            email="student@email.com",
            password="pwd123"
            )

        with self.assertRaises(Exception) as e:
            Student.objects.create(
                name="Any another name",
                registry="0000001",
                email="student@email.com",
                password="pwd1233"
            )

        self.assertEqual(len(Student.objects.all()), quantity + 1)

    # Admin
    def test_admin_creation(self):
        quantity = len(Admin.objects.all())
        Admin.objects.create(
            name="Any name",
            registry="0000000",
            email="student@email.com",
            password="pwd123"
        )

        self.assertEqual(len(Admin.objects.all()), quantity + 1)

    def test_admin_duplicate_email(self):
        quantity = len(Student.objects.all())
        Admin.objects.create(
            name="Any name",
            registry="0000000",
            email="student@email.com",
            password="pwd123"
            )

        with self.assertRaises(Exception) as e:
            Admin.objects.create(
                name="Any another name",
                registry="0000001",
                email="student@email.com",
                password="pwd1233"
            )

        self.assertEqual(len(Admin.objects.all()), quantity + 1)