# Generated by Django 3.2 on 2024-08-12 13:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompteUtilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Apprenant',
            fields=[
                ('matricule', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25)),
                ('postnom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('genre', models.CharField(max_length=1)),
                ('etatcivil', models.CharField(max_length=25)),
                ('addresse', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='ImageProfilApprenant/')),
            ],
            options={
                'db_table': 'Apprenant',
            },
        ),
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'Chapitre',
            },
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Domaine',
            },
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('matricule', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25)),
                ('postnom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('genre', models.CharField(max_length=1)),
                ('etatcivil', models.CharField(max_length=25)),
                ('addresse', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='ImageProfilEnseignant/')),
            ],
            options={
                'db_table': 'Enseignant',
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duree', models.CharField(max_length=20)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.domaine')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.enseignant')),
            ],
            options={
                'db_table': 'Formation',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.chapitre')),
            ],
            options={
                'db_table': 'Module',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'Niveau',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('reponse', models.TextField()),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.formation')),
            ],
            options={
                'db_table': 'Questionnaire',
            },
        ),
        migrations.CreateModel(
            name='Sous_chapitre',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('contenu', models.TextField()),
            ],
            options={
                'db_table': 'Sous_chapitre',
            },
        ),
        migrations.CreateModel(
            name='TypeRessource',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'TypeRessource',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('reponse', models.TextField()),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.apprenant')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.questionnaire')),
            ],
            options={
                'db_table': 'Test',
            },
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('contenu', models.FileField(max_length=500, upload_to='Ressource/')),
                ('type_ressource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.typeressource')),
            ],
            options={
                'db_table': 'Ressource',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='publication/')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Publication',
            },
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateTimeField()),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.apprenant')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.module')),
            ],
            options={
                'db_table': 'Paiement',
            },
        ),
        migrations.AddField(
            model_name='module',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.niveau'),
        ),
        migrations.AddField(
            model_name='module',
            name='ressource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eScholar.ressource'),
        ),
        migrations.CreateModel(
            name='ModalitePaie',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('tranche', models.CharField(max_length=25)),
                ('montant_fixe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.module')),
            ],
            options={
                'db_table': 'ModalitePaie',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='eScholar.publication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Like',
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('date_inscription', models.DateTimeField()),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.apprenant')),
                ('formation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eScholar.formation')),
                ('modalite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.modalitepaie')),
            ],
            options={
                'db_table': 'Inscription',
            },
        ),
        migrations.AddField(
            model_name='formation',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.module'),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('maximum', models.DecimalField(decimal_places=1, max_digits=10)),
                ('cote', models.DecimalField(decimal_places=1, max_digits=10)),
                ('date_evaluation', models.DateTimeField()),
                ('apprenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eScholar.apprenant')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.formation')),
            ],
            options={
                'db_table': 'Evaluation',
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='eScholar.publication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Commentaire',
            },
        ),
        migrations.AddField(
            model_name='chapitre',
            name='sous_chapitre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eScholar.sous_chapitre'),
        ),
        migrations.AddField(
            model_name='compteutilisateur',
            name='apprenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eScholar.apprenant'),
        ),
        migrations.AddField(
            model_name='compteutilisateur',
            name='enseignant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eScholar.enseignant'),
        ),
        migrations.AddField(
            model_name='compteutilisateur',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='compteutilisateur',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
