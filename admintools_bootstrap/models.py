
# monkey-pathching django admin

from django.contrib.admin import widgets
from django import forms

class FilteredSelectMultiple(forms.SelectMultiple):
    """
        removing 2 select fields widget
    """
    def __init__(self, verbose_name, is_stacked, attrs=None, choices=[]):
        super(FilteredSelectMultiple, self).__init__(attrs, choices)

widgets.FilteredSelectMultiple = FilteredSelectMultiple


# using jquery ui to display .vDateField

widgets.AdminDateWidget.media = None

# TODO: find why this breaks django admin
# class MyAdminDateWidget(widgets.AdminDateWidget):
#     def _media(self):
#         return forms.Media(js=['admintools_bootstrap/js/jquery-ui-timepicker-addon.js'])
#     media = property(_media)
# widgets.AdminDateWidget = MyAdminDateWidget


# patching admintools menu item

from admin_tools.menu import items

# adding icon argument to base MenuItem class
items.MenuItem.icon = None

import admintools_bootstrap.settings

# patching django's FieldSet
from django.contrib.admin import helpers
from django import forms


class Fieldset(helpers.Fieldset):
    def _media(self):
        if 'collapse' in self.classes:
            return forms.Media(js=['admintools_bootstrap/bootstrap/js/bootstrap-collapse.js'])
        return forms.Media()
    media = property(_media)

helpers.Fieldset = Fieldset
