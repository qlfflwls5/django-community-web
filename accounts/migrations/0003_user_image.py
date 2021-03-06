# Generated by Django 3.1.7 on 2021-04-06 16:15

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to='profile_images/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
