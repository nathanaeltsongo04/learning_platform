# Generated by Django 5.1 on 2024-08-22 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eScholar', '0014_reponsesalternativesinterro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interrogation',
            name='module',
        ),
        migrations.AddField(
            model_name='interrogation',
            name='formation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eScholar.formation'),
            preserve_default=False,
        ),
    ]
