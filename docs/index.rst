.. django-html-cleaner documentation master file, created by
   sphinx-quickstart on Tue Mar 11 15:32:10 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-html-cleaner's documentation!
===============================================

Quickstart
----------

Install django-html-cleaner::

    pip install django-html-cleaner

Then enable it in a Django project by adding ``django_html_cleaner`` to your
``INSTALLED_APPS`` in your Django settings.

Then use it::

    from django_html_cleaner.models import SanitizedTextField

    # in a Django model
    field = SanitizedTextField()

Django settings
---------------
``SanitizedCharField`` and ``SanitizedTextField`` can take an instance of
``django_html_cleaner.cleaner.Cleaner`` to set up how they will clean HTML
on save.

An alternative way to set this up is to use your Django settings. In
``django.conf.settings``, you can use the following settings to set up
django-html-cleaner's behavior:

``HTML_CLEANER_ALLOWED_TAGS``
  A list of tags that will be allowed. If not set, all tags
  that are known HTML tags and are not special (``script``, ``html``, etc)
  will be allowed.

``HTML_CLEANER_ALLOWED_ATTRIBUTES``
  A list of attributes that will be allowed. If not set, all attributes
  that are not JavaScript-related (``onclick``, for example) will be
  allowed.

``HTML_CLEANER_ALLOWED_STYLES``
  A list of styles that will be allowed. If not set, all styles are
  allowed.

``HTML_CLEANER_PARENT_TAG``
  If set to a tag name, all input will be wrapped in this parent tag.

Classes
-------

.. autoclass:: django_html_cleaner.cleaner.Cleaner
    :members: clean

.. automodule:: django_html_cleaner.models
    :members:
