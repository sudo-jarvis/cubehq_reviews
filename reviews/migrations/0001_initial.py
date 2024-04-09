# Generated by Django 4.2.11 on 2024-04-08 18:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('stars', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('review_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tone', models.CharField(max_length=255, null=True)),
                ('sentiment', models.CharField(max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.category')),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewhistory')),
            ],
        ),
    ]