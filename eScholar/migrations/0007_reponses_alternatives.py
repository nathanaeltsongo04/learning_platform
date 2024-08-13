# Generated by Django 3.2 on 2024-08-13 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eScholar', '0006_auto_20240813_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reponses_alternatives',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('reponse_alternative', models.CharField(max_length=255)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.questionnaire')),
            ],
            options={
                'db_table': 'Reponses_alternatives',
            },
        ),
    ]
