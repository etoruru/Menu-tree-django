# Generated by Django 4.1.5 on 2023-01-10 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuTree', '0002_alter_menuitem_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menuTree.menuitem'),
        ),
    ]
