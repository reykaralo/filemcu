# Generated by Django 4.1.3 on 2022-12-17 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('komen', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('artikel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.artikel')),
            ],
        ),
    ]
