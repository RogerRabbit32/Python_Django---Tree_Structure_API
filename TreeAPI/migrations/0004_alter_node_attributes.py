# Generated by Django 4.1.7 on 2023-03-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeAPI', '0003_alter_node_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='attributes',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
