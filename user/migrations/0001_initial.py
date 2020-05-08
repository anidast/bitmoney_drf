# Generated by Django 3.0.5 on 2020-05-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='photos')),
            ],
        ),
    ]
