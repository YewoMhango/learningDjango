# Generated by Django 4.0.2 on 2022-04-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_flower_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myapp.Tag'),
        ),
    ]
