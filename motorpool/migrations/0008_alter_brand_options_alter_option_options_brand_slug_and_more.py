# Generated by Django 4.0.5 on 2022-06-19 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0007_alter_auto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name': 'Опция', 'verbose_name_plural': 'Опции'},
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=210),
        ),
        migrations.AlterField(
            model_name='auto',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='auto',
            name='year',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepassport',
            name='auto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pts', to='motorpool.auto'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
