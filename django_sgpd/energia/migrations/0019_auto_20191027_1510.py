# Generated by Django 2.2 on 2019-10-27 15:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('energia', '0018_auto_20191026_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='ueb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energia.Ueb'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reading',
            name='for_meter',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='energia.Meter'),
        ),
    ]
