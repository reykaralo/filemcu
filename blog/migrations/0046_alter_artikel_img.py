# Generated by Django 4.1.3 on 2022-12-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='img'),
        ),
    ]
