# Generated by Django 4.1.5 on 2023-02-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_desc_place_detials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=200)),
                ('imge', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
