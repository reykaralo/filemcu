# Generated by Django 4.1.3 on 2022-12-09 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Filem',
            },
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
