# Generated by Django 2.2 on 2019-10-20 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energia', '0016_auto_20191016_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meter',
            name='consumption',
        ),
        migrations.AddField(
            model_name='reading',
            name='consumption',
            field=models.IntegerField(default=0),
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
