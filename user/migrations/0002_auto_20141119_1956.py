# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(default=user.models.my_random_key, null=True),
            preserve_default=True,
        ),
    ]
