# Generated by Django 3.2.6 on 2022-04-17 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='name',
            new_name='first_name',
        ),
    ]