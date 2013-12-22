Django-cbvpatterns
==================

A nicer version of `patterns()` for use with class based views. Inspired
largely by Loic.

What is this?
-------------

If you're a big fan of class based views in Django, you might often find your
urls.py starting to look a little cluttered. Something like::

    from django.conf.urls import patterns, url

    from ponies import views


    urlpatterns = patterns('',
        url(r'^$', views.Index.as_view(), name='index'),
        url(r'^ponies/$', views.PonyList.as_view(), name='pony-list'),
        url(r'^ponies/create/$', views.PonyCreate.as_view(), name='pony-create'),
        url(r'^ponies/(?P<pk>\d+)/$', views.PonyDetail.as_view(), name='pony-detail'),
        url(r'^ponies/(?P<pk>\d+)/edit/$', views.PonyUpdate.as_view(), name='pony-update'),
    )

The shortcuts you can use in patterns are really functional-view specific. The
functional version looks much nicer::

    from django.conf.urls import patterns, url


    urlpatterns = patterns('ponies.views',
        url(r'^$', 'index', name='index'),
        url(r'^ponies/$', 'pony_list', name='pony-list'),
        url(r'^ponies/create/$', 'pony_create', name='pony-create'),
        url(r'^ponies/(?P<pk>\d+)/$', 'pony_detail', name='pony-detail'),
        url(r'^ponies/(?P<pk>\d+)/edit/$', 'pony_update, name='pony-update'),
    )

So we can now have a class based view version which has the same feel::

    from cbvpatterns import patterns, url


    urlpatterns = patterns('ponies.views',
        url(r'^$', 'Index', name='index'),
        url(r'^ponies/$', 'PonyList', name='pony-list'),
        url(r'^ponies/create/$', 'PonyCreate', name='pony-create'),
        url(r'^ponies/(?P<pk>\d+)/$', 'PonyDetail', name='pony-detail'),
        url(r'^ponies/(?P<pk>\d+)/edit/$', 'PonyUpdate, name='pony-update'),
    )

You can also pass in the actual view classes directly, rather than using the
string representation.

Contributing
------------

Development takes place
`on GitHub <http://github.com/mjtamlyn/django-cbvpatterns>`_; pull requests are
welcome. Run tests with `tox <http://tox.readthedocs.org/>`_.
