# Generated by Django 4.1.3 on 2022-12-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_rename_comment_komen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Komen',
            new_name='Comment',
        ),
    ]
