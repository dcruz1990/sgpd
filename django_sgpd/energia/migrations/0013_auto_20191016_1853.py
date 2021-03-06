# Generated by Django 2.2 on 2019-10-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energia', '0012_auto_20191013_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='prev_reading',
        ),
        migrations.AlterField(
            model_name='meter',
            name='ueb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energia.Ueb'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='meter',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='energia.Meter'),
        ),
    ]
