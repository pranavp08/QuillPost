# Generated by Django 4.2.6 on 2023-11-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.BigIntegerField(),
        ),
    ]
