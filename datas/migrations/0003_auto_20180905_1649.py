# Generated by Django 2.0.6 on 2018-09-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0002_auto_20180725_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='canteen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.CharField(default=0, max_length=20)),
                ('bill', models.IntegerField(default=0)),
                ('payment_option', models.CharField(default=0, max_length=20)),
                ('order_status', models.CharField(default=0, max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='ie',
        ),
    ]
