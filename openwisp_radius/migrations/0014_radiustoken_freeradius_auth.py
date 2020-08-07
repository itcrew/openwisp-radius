# Generated by Django 3.0.7 on 2020-06-30 19:46

import django.db.models.deletion
from django.db import migrations, models
from swapper import get_model_name

from . import delete_old_radius_token


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_radius', '0013_remove_null_uuid_field'),
    ]

    operations = [
        migrations.RunPython(
            delete_old_radius_token, reverse_code=migrations.RunPython.noop
        ),
        migrations.AddField(
            model_name='radiustoken',
            name='can_auth',
            field=models.BooleanField(
                default=False,
                help_text='Enable the radius token to be used for freeradius authorization request',
            ),
        ),
        migrations.AddField(
            model_name='radiustoken',
            name='organization',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=get_model_name('openwisp_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
    ]
