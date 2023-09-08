import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from .admin import UserCreationForm
from .models import MyUserManager, User
from .serializers import RegisterSerializer
from .views import RegisterAPIView


class TestModel(APITestCase):
    def test_valid_form_creates_user_and_saves(self):
        form_data = {
            "email": "test@example.com",
            "date_of_birth": "1990-01-01",
            "password1": "password123",
            "password2": "password123",
        }

        form = UserCreationForm(data=form_data)

        # Assert
        assert form.is_valid()
        user = form.save()
        assert user.email == "test@example.com"
        assert str(user.date_of_birth) == '1990-01-01'
        assert user.check_password("password123")

    def test_raise_when_invalid_form_passwords_dont_match(self):
        form_data = {
            "email": "test@example.com",
            "date_of_birth": "1990-01-01",
            "password1": "password123",
            "password2": "differentpassword",
        }
        form = UserCreationForm(data=form_data)

        # Assert
        assert not form.is_valid()
        assert "password2" in form.errors

    def test_create_user_raise_when_email_is_empty(self):
        # Arrange
        user_manager = MyUserManager()
        email = ""
        date_of_birth = "1990-01-01"
        password = "password123"

        # Assert
        self.assertRaises(
            ValueError, user_manager.create_user, email, date_of_birth, password
        )

    def test_create_user_raise_when_date_of_birth_is_empty(self):
        # Arrange
        user_manager = MyUserManager()
        email = "test@example.com"
        date_of_birth = ""
        password = "password123"

        # Assert
        self.assertRaises(
            ValueError, user_manager.create_user, email, date_of_birth, password
        )

    def test_creates_user(self):
        user = User.objects.create_user(
            'test@example.com',
            date_of_birth="1990-01-01",
            password="password123",
        )
        perm = "perm_test0083023899700"
        app_label = "app_label_test02020203376602"

        # Assert
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.has_perm(perm=perm, obj=None))
        self.assertTrue(user.has_module_perms(app_label=app_label))
        self.assertEqual(user.email, 'test@example.com')

    def test_creates_super_user(self):
        superuser = User.objects.create_superuser(
            'test@example.com',
            date_of_birth="1990-01-01",
            password="password123",
        )
        perm = "perm_test29736152"
        app_label = "app_label_test328936"

        # Assert
        self.assertIsInstance(superuser, User)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.has_perm(perm=perm, obj=None))
        self.assertTrue(superuser.has_module_perms(app_label=app_label))
        self.assertEqual(superuser.__str__(), 'test@example.com')
        self.assertEqual(superuser.email, 'test@example.com')

    def test_create_user_with_valid_data(self):
        serializer = RegisterSerializer()
        data = {
            'first_name': 'Sinbad',
            'last_name': 'Bahri',
            'email': 'sinbadBahri@example.com',
            'date_of_birth': '1997-11-25',
            'language': 1,
            'company': 'Sinbad Industries',
            'password': 'password123'
        }
        user = serializer.create(data)

        # Asserts
        assert user.first_name == 'Sinbad'
        assert user.last_name == 'Bahri'
        assert user.email == 'sinbadBahri@example.com'
        assert user.date_of_birth == str(datetime.date(1997, 11, 25))
        assert user.language == 1
        assert user.company == 'Sinbad Industries'

    def test_duplicate_email(self):
        # Arrange
        register_api_view = RegisterAPIView()

        class Request:
            def __str__(self):
                return "TEST CLASS"

        test_data = {
            'first_name': 'Sinbad',
            'last_name': 'Bahri',
            'email': 'sinbadBahri@example.com',
            'date_of_birth': '1998-11-25',
            'language': 4,
            'company': '',
            'password': 'password123'
        }

        request = Request()
        request.data = test_data

        # Act
        response1 = register_api_view.post(request)
        response2 = register_api_view.post(request)

        # Assert
        assert response1.status_code == status.HTTP_201_CREATED
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
