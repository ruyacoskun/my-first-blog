# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
                ('yaratilis_tarihi', models.DateTimeField(default=django.utils.timezone.now)),
                ('yayinlanma_tarihi', models.DateTimeField(blank=True, null=True)),
                ('yazar', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
