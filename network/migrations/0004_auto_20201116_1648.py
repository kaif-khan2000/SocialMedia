# Generated by Django 3.1 on 2020-11-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20201114_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default='static/img/profile_pic.png', null=True, upload_to='static/profile'),
        ),
    ]
