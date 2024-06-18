# Generated by Django 5.0.6 on 2024-06-17 14:07

import django.db.models.deletion
import product.helpes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('speciality', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=product.helpes.SaveImagesTeam.team_images_path)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='product_tea_id_0d4a76_idx')],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to=product.helpes.SaveImagesBlog.blog_images_path)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.team')),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='product_blo_id_ad0704_idx')],
            },
        ),
    ]
