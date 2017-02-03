from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class BlogListTest(TestCase):
    """
    Testing rss and atom feeds.
    """
    def test_blog_feed_rss(self):
        client = Client()
        response = client.get(reverse('rss'))
        self.assertEqual(response.status_code, 200)

    def test_blog_feed_atom(self):
        client = Client()
        response = client.get(reverse('atom'))
        self.assertEqual(response.status_code, 200)
