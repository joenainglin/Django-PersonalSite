# Generated by Django 2.1.1 on 2018-11-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sslug', models.SlugField(unique=True)),
                ('body', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='Posts/%Y/%m/%d/')),
            ],
        ),
    ]
