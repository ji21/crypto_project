# Generated by Django 3.1 on 2020-09-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_account_new_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='in_progress',
            field=models.BooleanField(default=True),
        ),
    ]
