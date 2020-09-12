# Generated by Django 3.1 on 2020-09-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20200910_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount_earned',
            new_name='amount_earned_btc',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='market_price_sell',
            new_name='amount_earned_eur',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_fee',
            new_name='amount_earned_gdp',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='created',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='market_price_buy',
        ),
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount_earned_usd',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='market_price_buy_eur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='market_price_buy_gdp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='market_price_buy_usd',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='market_price_sell_eur',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='market_price_sell_gdp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='market_price_sell_usd',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
