# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='show_in_calendar',
            field=models.BooleanField(default=True, verbose_name='Show in calendar'),
        ),
    ]
