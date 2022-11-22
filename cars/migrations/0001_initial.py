# Generated by Django 4.1.2 on 2022-11-20 16:01

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('city', models.CharField(choices=[('TASH', 'Tashkent'), ('SAM', 'Samarkand'), ('NAM', 'Namangan'), ('AND', 'Andijan'), ('JIZ', 'Jizzakh'), ('FER', 'Fergana'), ('BUKH', 'Bukhara'), ('QAR', 'Qarshi'), ('KOK', 'Kokand'), ('NAV', 'Navoi'), ('SYR', 'Syrdarya')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('car_photo', models.ImageField(upload_to='media/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='media/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='media/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='media/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='media/')),
                ('features', models.CharField(choices=[('Tanirovka', 'Tanirovka'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Malibu Bar', 'Malibu Bar'), ('Airbag', 'Airbag'), ('Power Steering', 'Power Steering'), ('Avtoregistartr', 'Avtoregistratr'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Planshet ekran', 'Planshen ekran')], max_length=255)),
                ('transmission', models.CharField(max_length=100)),
                ('body_style', models.CharField(max_length=255)),
                ('engine', models.CharField(max_length=255)),
                ('interior', models.CharField(max_length=255)),
                ('km', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('4', '4')], max_length=10)),
                ('passengers', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
    ]
