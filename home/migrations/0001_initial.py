# Generated by Django 5.0.6 on 2024-06-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('activity_level', models.CharField(choices=[('sedentary', 'Sedentary'), ('lightly_active', 'Lightly Active'), ('active', 'Active'), ('very_active', 'Very Active')], max_length=20)),
                ('goal', models.CharField(choices=[('weight_loss', 'Weight Loss'), ('weight_gain', 'Weight Gain'), ('maintenance', 'Maintenance')], max_length=20)),
            ],
        ),
    ]
