# Generated by Django 3.1.1 on 2020-11-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='email',
            field=models.EmailField(default='name@default.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
