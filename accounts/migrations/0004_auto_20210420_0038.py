# Generated by Django 3.1.7 on 2021-04-19 15:38

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='profile_images/%Y/%m/%d/'),
        ),
    ]
