# Generated by Django 2.0.4 on 2018-04-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('0', 'Current'), ('1', 'Saving')], default='1', max_length=1),
        ),
    ]