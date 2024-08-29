# Generated by Django 5.1 on 2024-08-28 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eScholar', '0016_alter_participation_cote_obtenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('apprenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_as_apprenant', to=settings.AUTH_USER_MODEL)),
                ('enseignant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations_as_enseignant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Conversation',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='eScholar.conversation')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Message',
            },
        ),
    ]
