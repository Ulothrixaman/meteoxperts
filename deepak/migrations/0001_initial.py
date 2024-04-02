# Generated by Django 5.0.1 on 2024-01-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('pro_img', models.ImageField(upload_to='products/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('about', models.TextField()),
                ('dis_price', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('model_name', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=20)),
                ('datasheet', models.FileField(upload_to='datasheets/')),
                ('manual', models.FileField(upload_to='manuals/')),
                ('url', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]