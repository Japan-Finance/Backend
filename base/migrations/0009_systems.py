# Generated by Django 4.2.1 on 2023-05-30 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_french'),
    ]

    operations = [
        migrations.CreateModel(
            name='systems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.TextField()),
                ('user_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
        ),
    ]
