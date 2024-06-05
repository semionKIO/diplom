# Generated by Django 5.0.3 on 2024-05-15 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wewe', '0002_services_left_services_right'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Описание работника')),
                ('main', models.ImageField(upload_to='images/')),
                ('left', models.ImageField(default='path/to/my/default/image.jpg', upload_to='images/')),
                ('right', models.ImageField(default='path/to/my/default/image.jpg', upload_to='images/')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Работника',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RenameField(
            model_name='services',
            old_name='car',
            new_name='main',
        ),
    ]
