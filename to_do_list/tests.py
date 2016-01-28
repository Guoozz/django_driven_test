from django.test import TestCase
from to_do_list.views import index
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.

class IndexTest(TestCase):

    def test_index_url_visits_with_slash(self):
        found = resolve('/')
        self.assertEqual(found.func,index)
        
    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        excepted_html = render_to_string('to_do_list/index.html')
        self.assertEqual(excepted_html,response.content.decode())
