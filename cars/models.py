from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField




class CarModel(models.Model):
    city_choice = (
        ('TASH', 'Tashkent'),
        ('SAM', 'Samarkand'),
        ('NAM', 'Namangan'),
        ('AND', 'Andijan'),
        ('JIZ', 'Jizzakh'),
        ('FER', 'Fergana'),
        ('BUKH', 'Bukhara'),
        ('QAR', 'Qarshi'),
        ('KOK', 'Kokand'),
        ('NAV', 'Navoi'),
        ('SYR', 'Syrdarya'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Tanirovka', 'Tanirovka'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Malibu Bar', 'Malibu Bar'),
        ('Airbag', 'Airbag'),
        ('Power Steering', 'Power Steering'),
        ('Avtoregistartr', 'Avtoregistratr'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Planshet ekran', 'Planshen ekran'),
    )

    door_choices = (
        ('2', '2'),
        ('4', '4'),
    )
    car_title = models.CharField(max_length=255)
    city = models.CharField(choices=city_choice, max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='media/')
    car_photo_1 = models.ImageField(upload_to='media/', blank=True)
    car_photo_2 = models.ImageField(upload_to='media/', blank=True)
    car_photo_3 = models.ImageField(upload_to='media/', blank=True)
    car_photo_4 = models.ImageField(upload_to='media/', blank=True)
    features = MultiSelectField(max_length=255, choices=features_choices)
    transmission = models.CharField(max_length=100)
    body_style = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    km = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return self.car_title


    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'
