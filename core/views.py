from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext


def home(request):
    count = 1
    _name = 'Person'

    title = _('Title goes here %(count)s') % {'count': count}

    plurals = ungettext(
        'There is %(count)s person here',
        'There are %(count)s people here',
        count) % {'count': count}

    stringiii = _('%(name)s is not cool' % {'name': _name})

    data = {
        'welcome': _('Welcome home friends'),
        'name': stringiii,
        'plural': plurals,
        'count': count,
        'a_name': _name,
        'title': title
    }

    return render(request, 'index.html', data)
