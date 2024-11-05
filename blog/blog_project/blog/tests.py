from blog.models import Post
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")

    def test_register(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "password": "newpassword",
                "password_confirm": "newpassword",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login(self):
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "testpass"}
        )

        self.assertRedirects(response, reverse("home"))

        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Witaj, testuser!")

    def test_create_post(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("create_post"),
            {"title": "Test Post", "content": "This is a test post."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Test Post").exists())

    def test_posts_home(self):
        self.client.login(username="testuser", password="testpass")
        Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )
        response = self.client.get(reverse("posts_home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/posts_home.html")
        self.assertContains(response, "Test Post")
