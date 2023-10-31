# Generated by Django 3.2.16 on 2022-12-29 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dssProject', '0006_auto_20221229_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantencion',
            name='semana',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantencion',
            name='fecha',
            field=models.CharField(max_length=500),
        ),
    ]