from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver, get_callable
from django.utils import six
from django.views.generic import View


class CBVRegexURLPattern(RegexURLPattern):
    _callback_processed = None

    @property
    def callback(self):
        if self._callback_processed is not None:
            return self._callback
        if getattr(self, '_callback_str', None) is not None:
            self._callback = get_callable(self._callback_str)
        if isinstance(self._callback, type) and issubclass(self._callback, View):
            self._callback = self._callback.as_view()
        else:
            self._callback = self._callback
        self._callback_processed = True
        return self._callback


def patterns(prefix, *args):
    """As patterns() in django."""
    pattern_list = []
    for t in args:
        if isinstance(t, (list, tuple)):
            t = url(prefix=prefix, *t)
        elif isinstance(t, RegexURLPattern):
            t.add_prefix(prefix)
        pattern_list.append(t)
    return pattern_list


def url(regex, view, kwargs=None, name=None, prefix=''):
    """As url() in Django."""
    if isinstance(view, (list, tuple)):
        # For include(...) processing.
        urlconf_module, app_name, namespace = view
        return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)
    else:
        if isinstance(view, six.string_types):
            if not view:
                raise ImproperlyConfigured('Empty URL pattern view name not permitted (for pattern %r)' % regex)
            if prefix:
                view = prefix + '.' + view
            view = get_callable(view)
        return CBVRegexURLPattern(regex, view, kwargs, name)
