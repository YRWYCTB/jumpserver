# Generated by Django 2.2.13 on 2020-08-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20200728_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('Admin', 'System administrator'), ('User', 'User'), ('Auditor', 'System auditor'), ('App', 'Application')], default='User', max_length=10, verbose_name='Role'),
        ),
    ]
