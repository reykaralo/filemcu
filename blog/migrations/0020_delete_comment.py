# Generated by Django 4.1.3 on 2022-12-14 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
