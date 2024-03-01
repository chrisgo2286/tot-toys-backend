# Generated by Django 5.0.1 on 2024-01-31 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
