# Generated by Django 3.2.7 on 2021-09-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'nota', 'verbose_name_plural': 'notas'},
        ),
        migrations.AddField(
            model_name='post',
            name='key',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]