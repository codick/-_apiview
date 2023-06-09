# Generated by Django 4.2b1 on 2023-03-20 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('born_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(max_length=100)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.director')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='genre', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('films', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.films')),
            ],
        ),
        migrations.AddField(
            model_name='films',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.genre'),
        ),
    ]
