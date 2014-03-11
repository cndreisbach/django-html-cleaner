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

Classes
-------

.. autoclass:: django_html_cleaner.cleaner.Cleaner
    :members: clean

.. automodule:: django_html_cleaner.models
    :members:
