# Generated by Django 3.0.8 on 2020-07-15 01:34

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('closings', '0004_auto_20200714_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmlocation',
            name='city',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='state', on_delete=django.db.models.deletion.CASCADE, to='closings.City'),
        ),
    ]
