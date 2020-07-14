# Generated by Django 2.2 on 2019-10-13 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energia', '0006_auto_20191013_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reading',
            old_name='_date',
            new_name='date',
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
