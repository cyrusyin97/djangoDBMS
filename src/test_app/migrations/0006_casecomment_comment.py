# Generated by Django 3.0.4 on 2020-04-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_auto_20200419_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='casecomment',
            name='comment',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]