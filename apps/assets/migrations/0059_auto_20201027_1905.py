# Generated by Django 2.2.13 on 2020-10-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0058_auto_20201023_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='protocol',
            field=models.CharField(choices=[('ssh', 'ssh'), ('rdp', 'rdp'), ('telnet', 'telnet'), ('vnc', 'vnc'), ('mysql', 'mysql'), ('oracle', 'oracle'), ('mariadb', 'mariadb'), ('postgresql', 'postgresql'), ('k8s', 'k8s')], default='ssh', max_length=16, verbose_name='Protocol'),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='ad_domain',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='ip',
            field=models.CharField(db_index=True, max_length=128, verbose_name='IP'),
        ),
    ]
