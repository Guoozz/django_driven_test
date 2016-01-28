from django.test import TestCase
from to_do_list.views import index
from django.core.urlresolvers import resolve
from django.http import HttpRequest
# Create your tests here.

class IndexTest(TestCase):

    def test_index_url_visits_with_slash(self):
        found = resolve('/')
        self.assertEqual(found.func,index)
        
    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
