# Generated by Django 4.0.5 on 2022-08-13 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0008_alter_brand_options_alter_option_options_brand_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='motorpool/brands/'),
        ),
        migrations.AlterField(
            model_name='vehiclepassport',
            name='auto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pts', to='motorpool.auto', verbose_name='Автомобиль'),
        ),
    ]
