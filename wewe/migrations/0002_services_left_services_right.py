# Generated by Django 5.0.3 on 2024-05-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wewe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='left',
            field=models.ImageField(default='path/to/my/default/image.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='services',
            name='right',
            field=models.ImageField(default='path/to/my/default/image.jpg', upload_to='images/'),
        ),
    ]