# Generated by Django 3.2.7 on 2021-09-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20210919_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='key',
            new_name='subtitle',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]