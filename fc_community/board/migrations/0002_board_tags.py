# Generated by Django 2.2.4 on 2019-09-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20190901_0720'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag', verbose_name='태그'),
        ),
    ]
