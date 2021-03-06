# Generated by Django 2.2.6 on 2019-10-04 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ueb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('month_plan', models.IntegerField()),
                ('day_plan', models.IntegerField()),
                ('reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energia.reading')),
                ('ueb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energia.ueb')),
            ],
        ),
    ]
