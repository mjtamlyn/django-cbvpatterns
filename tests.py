import unittest

from django.conf import settings

if __name__ == '__main__':
    # has to be here or I can't import View
    settings.configure()

from django.core.urlresolvers import RegexURLResolver
from django.views.generic import View

from cbvpatterns import patterns, url


class TestView(View):
    def dispatch(self, request, *args, **kwargs):
        return 'Success!'


no_prefix_patterns = patterns('',
    url('^1/$', TestView.as_view()),
    url('^2/$', TestView),
    url('^3/$', 'tests.TestView'),
)


prefix_patterns = patterns('tests',
    url('^1/$', TestView.as_view()),
    url('^2/$', TestView),
    url('^3/$', 'TestView'),
)

no_url_patterns = patterns('',
    ('^1/$', TestView.as_view()),
)


class PatternsTests(unittest.TestCase):

    def test_no_prefix_view_function(self):
        resolver = RegexURLResolver('/', no_prefix_patterns)
        view = resolver.resolve('/1/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')

    def test_no_prefix_view_class(self):
        resolver = RegexURLResolver('/', no_prefix_patterns)
        view = resolver.resolve('/2/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')

    def test_no_prefix_string(self):
        resolver = RegexURLResolver('/', no_prefix_patterns)
        view = resolver.resolve('/3/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')

    def test_prefix_view_function(self):
        resolver = RegexURLResolver('/', prefix_patterns)
        view = resolver.resolve('/1/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')

    def test_prefix_view_class(self):
        resolver = RegexURLResolver('/', prefix_patterns)
        view = resolver.resolve('/2/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')

    def test_prefix_string(self):
        resolver = RegexURLResolver('/', prefix_patterns)
        view = resolver.resolve('/3/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')

    def test_no__patterns(self):
        resolver = RegexURLResolver('/', no_url_patterns)
        view = resolver.resolve('/1/')[0]
        response = view(None)
        self.assertEqual(response, 'Success!')


if __name__ == '__main__':
    unittest.main()
