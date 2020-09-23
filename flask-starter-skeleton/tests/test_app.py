from unittest import TestCase, main

from app import db, create_app
from app.models import User

app = create_app(environment='testing')


class TestApp(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_ctx.pop()

    def register(self, username, email, password='password', confirmation='password'):
        return self.client.post(
            '/register', data=dict(
                username=username,  email=email, password=password,
                password_confirmation=confirmation),
            follow_redirects=True)

    def login(self, user_id, password='password'):
        return self.client.post(
            '/login', data=dict(user_id=user_id, password=password),
            follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        # Valid data should register successfully.
        response = self.register('alice', 'alice@example.com')
        self.assertIn(b'Registration successful. You are logged in.', response.data)
        # Password/Confirmation mismatch should fail.
        response = self.register('bob', 'bob@example.org', 'password', 'Password')
        self.assertIn(b'The given data was invalid.', response.data)
        # Existing username registration should fail.
        response = self.register('alice', 'alice01@example.com',)
        self.assertIn(b'The given data was invalid.', response.data)
        # Existing email registration should fail.
        response = self.register('alicia', 'alice@example.com')
        self.assertIn(b'The given data was invalid.', response.data)

    def test_login_and_logout(self):
        # Access to logout view before login should fail.
        response = self.logout()
        self.assertIn(b'Please log in to access this page.', response.data)
        # New user will be automatically logged in.
        self.register('sam', 'sam@example.com')
        # Should successfully logout the currently logged in user.
        response = self.logout()
        self.assertIn(b'You were logged out.', response.data)
        # Incorrect login credentials should fail.
        response = self.login('sam@example.com', 'wrongpassword')
        self.assertIn(b'Wrong user ID or password.', response.data)
        # Correct credentials should login
        response = self.login('sam')
        self.assertIn(b'Login successful.', response.data)


if __name__ == "__main__":
    main()
