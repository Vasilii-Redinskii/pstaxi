# Generated by Django 4.0.5 on 2022-06-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0006_alter_auto_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='options',
            field=models.ManyToManyField(related_name='cars', to='motorpool.option'),
        ),
    ]