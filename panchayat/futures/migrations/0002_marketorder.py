# Generated by Django 2.2.5 on 2019-12-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CropName', models.CharField(max_length=50)),
                ('CropVariety', models.CharField(max_length=50)),
                ('Quantity', models.PositiveIntegerField(default=None)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('ClosingDate', models.DateField()),
                ('ProductionMode', models.CharField(max_length=50)),
                ('BasePrice', models.FloatField(default=None)),
                ('OrderStatus', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=10)),
            ],
        ),
    ]
