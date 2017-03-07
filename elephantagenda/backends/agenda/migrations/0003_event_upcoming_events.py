# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_event_show_in_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='upcoming_events',
            field=models.BooleanField(default=True, verbose_name=b'P\xc5\x99ipravovan\xc3\xa9 akce'),
        ),
    ]
