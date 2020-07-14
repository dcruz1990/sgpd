# Generated by Django 2.2 on 2019-10-27 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energia', '0021_auto_20191027_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='ueb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energia.Ueb'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='for_meter',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='energia.Meter'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='reading',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
