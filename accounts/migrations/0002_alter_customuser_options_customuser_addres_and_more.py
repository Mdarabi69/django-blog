# Generated by Django 4.2 on 2024-02-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='addres',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='سن'),
        ),
    ]
