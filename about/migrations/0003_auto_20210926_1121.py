# Generated by Django 3.2.7 on 2021-09-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210926_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='oy',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='article',
            name='single_photo',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='yil',
            field=models.SmallIntegerField(),
        ),
    ]