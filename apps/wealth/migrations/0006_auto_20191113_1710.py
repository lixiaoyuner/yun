# Generated by Django 2.2.7 on 2019-11-13 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wealth', '0005_auto_20191112_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='delist_date',
            field=models.DateField(blank=True, null=True, verbose_name='退市日期'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='list_date',
            field=models.DateField(verbose_name='上市日期'),
        ),
        migrations.CreateModel(
            name='DayK',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trade_date', models.DateField(verbose_name='上市日期')),
                ('open', models.FloatField(verbose_name='开盘价')),
                ('hign', models.FloatField(verbose_name='最高价')),
                ('low', models.FloatField(verbose_name='最低价')),
                ('close', models.FloatField(verbose_name='收盘价')),
                ('pre_close', models.FloatField(verbose_name='昨收价')),
                ('change', models.FloatField(verbose_name='涨跌额')),
                ('pct_chg', models.FloatField(verbose_name='涨跌幅')),
                ('vol', models.FloatField(verbose_name='成交量（手）')),
                ('amount', models.FloatField(verbose_name='成交额（千元）')),
                ('stock', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='wealth.Stock', verbose_name='对应股票')),
            ],
            options={
                'verbose_name': '所有股票日K信息',
                'verbose_name_plural': '所有股票日K信息',
                'ordering': ('id',),
            },
        ),
    ]