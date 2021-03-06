# Generated by Django 3.1 on 2020-08-24 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='fee',
            new_name='market_price',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='to',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='user_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='crypto.user'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='crypto.user'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='crypto.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='api_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
