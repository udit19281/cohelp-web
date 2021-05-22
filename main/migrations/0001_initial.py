# Generated by Django 3.2.1 on 2021-05-22 11:14

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
            name='User',
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
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('contact_person', models.CharField(default='NA', max_length=100)),
                ('address', models.CharField(default='NA', max_length=70)),
                ('pincode', models.IntegerField(default=0)),
                ('status', models.CharField(default='NA', max_length=100)),
                ('link', models.URLField(default='http://')),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Ambulance',
            },
        ),
        migrations.CreateModel(
            name='BloodPlasma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('contact_person', models.CharField(default='NA', max_length=100)),
                ('address', models.CharField(default='NA', max_length=70)),
                ('link', models.URLField(default='http://')),
                ('medical_conditions', models.CharField(default='NA', max_length=70)),
                ('availibility_status', models.CharField(default='NA', max_length=100)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Bloodplasma',
            },
        ),
        migrations.CreateModel(
            name='EConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=50)),
                ('contact_number', models.IntegerField()),
                ('area', models.CharField(default='NA', max_length=200)),
                ('contact_person', models.CharField(default='NA', max_length=100)),
                ('status', models.CharField(default='NA', max_length=200)),
                ('last_verified', models.DateTimeField()),
            ],
            options={
                'db_table': 'Econsultation',
            },
        ),
        migrations.CreateModel(
            name='FoodSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('contact_person', models.CharField(default='NA', max_length=100)),
                ('address', models.CharField(default='NA', max_length=70)),
                ('status', models.CharField(default='NA', max_length=100)),
                ('no_of_meals', models.IntegerField(default=0)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Foodsupport',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=50)),
                ('pharmacy', models.CharField(default='NA', max_length=100)),
                ('contact_number', models.IntegerField()),
                ('status', models.CharField(default='NA', max_length=100)),
                ('last_verified', models.DateTimeField()),
            ],
            options={
                'db_table': 'Medicine',
            },
        ),
        migrations.CreateModel(
            name='Oxygen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=50)),
                ('contact_number', models.IntegerField()),
                ('area', models.CharField(default='NA', max_length=200)),
                ('contact_person', models.CharField(default='NA', max_length=100)),
                ('status', models.CharField(default='NA', max_length=50)),
                ('last_verified', models.DateField()),
            ],
            options={
                'db_table': 'Oxygen',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact_number', models.IntegerField()),
                ('contact_person', models.CharField(default='NA', max_length=100)),
                ('hospital_admission_status', models.BooleanField()),
                ('hospital_name', models.CharField(max_length=50)),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_contactnum', models.IntegerField()),
                ('requirement', models.CharField(max_length=50)),
                ('caretaker_number', models.IntegerField()),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='PlasmaXchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=50)),
                ('PatientAge', models.IntegerField()),
                ('PatientBloodGroup', models.CharField(max_length=3)),
                ('PatientContact', models.IntegerField()),
                ('PatientAddress', models.CharField(max_length=200)),
                ('DonorName', models.CharField(max_length=50)),
                ('DonorAge', models.IntegerField()),
                ('DonorBloodGroup', models.CharField(max_length=3)),
                ('DonorContact', models.IntegerField()),
                ('DonorAddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Plasmaxchange',
            },
        ),
        migrations.CreateModel(
            name='RequestedResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(choices=[('Oxygen', 'Oxygen'), ('Bloodplasma', 'Bloodplasma'), ('Foodsupport', 'Foodsupport'), ('Econsultation', 'Econsultation'), ('Medicine', 'Medicine')], max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Ok', 'Ok'), ('Failed', 'Failed')], default='Pending', max_length=50)),
            ],
            options={
                'db_table': 'RequestedResource',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
