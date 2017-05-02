# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-25 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='enable_form',
            new_name='enable_forum',
        ),
        migrations.AddField(
            model_name='challenge',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='challenge_creator', to='hosts.ChallengeHostTeam'),
            preserve_default=False,
        ),
    ]
