# Generated by Django 4.2.5 on 2023-09-20 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_classes_product_kelas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='amount',
            new_name='jumlah_mahasiswa',
        ),
    ]
