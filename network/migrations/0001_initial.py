# Generated by Django 3.1 on 2020-11-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.IntegerField()),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('bio', models.TextField()),
                ('profile_pic', models.FileField(upload_to='static/profile')),
                ('relationship_status', models.CharField(max_length=35)),
                ('profession', models.CharField(max_length=100)),
                ('profile_status', models.CharField(max_length=15)),
                ('validation_otp', models.CharField(max_length=8)),
            ],
        ),
    ]
