# Generated by Django 4.2.5 on 2023-09-27 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_header_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_img',
            new_name='header_image',
        ),
    ]
