# Generated by Django 2.2.14 on 2022-08-05 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20220805_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='count',
            field=models.IntegerField(default=1, verbose_name='点击次数'),
        ),
    ]
