from django.conf import settings
from django.db import models
from django.utils.encoding import smart_unicode
from . import cleaner


class SanitizedCharField(models.CharField):

    def __init__(self, cleaner=cleaner.Cleaner(), *args, **kwargs):
        self.cleaner = cleaner
        super(SanitizedCharField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(SanitizedCharField, self).to_python(value)
        value = self.cleaner(value)
        return smart_unicode(value)


class SanitizedTextField(models.TextField):

    def __init__(self, cleaner=cleaner.Cleaner(), *args, **kwargs):
        self.cleaner = cleaner
        super(SanitizedTextField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        value = super(SanitizedTextField, self).to_python(value)
        value = self.cleaner(value)
        return smart_unicode(value)

    def get_prep_value(self, value):
        value = super(SanitizedTextField, self).get_prep_value(value)
        value = self.cleaner(value)
        return value


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^sanitizer\.models\.SanitizedCharField"])
    add_introspection_rules([], ["^sanitizer\.models\.SanitizedTextField"])
