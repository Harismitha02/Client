# Generated by Django 4.1.7 on 2023-03-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userReg', '0002_auto_20230319_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previl',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]