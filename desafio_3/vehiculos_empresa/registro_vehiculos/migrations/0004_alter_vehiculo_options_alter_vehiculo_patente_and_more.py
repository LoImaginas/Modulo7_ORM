# Generated by Django 5.0.6 on 2024-07-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_vehiculos', '0003_alter_vehiculo_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name_plural': 'Vehiculos'},
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='patente',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2024),
        ),
    ]