from django.test import TestCase
from to_do_list.views import index
from django.core.urlresolvers import resolve
# Create your tests here.

class IndexTest(TestCase):

    def test_index_url_visits_with_slash(self):
        found = resolve('/')
        self.assertEqual(found.func,index)
        

