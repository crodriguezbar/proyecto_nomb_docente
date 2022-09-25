# Generated by Django 4.1 on 2022-09-24 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_nomb_doc', '0010_alter_comisiones_options_remove_asignaturas_carrera_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignaturas',
            options={'verbose_name': 'Asignatura', 'verbose_name_plural': 'Asignaturas'},
        ),
        migrations.AlterModelOptions(
            name='carreras',
            options={'verbose_name': 'Carrera', 'verbose_name_plural': 'Carreras'},
        ),
        migrations.AlterModelOptions(
            name='docentes',
            options={'verbose_name': 'Docente', 'verbose_name_plural': 'Docentes'},
        ),
        migrations.AlterModelTable(
            name='asignaturas',
            table='Asignaturas',
        ),
        migrations.AlterModelTable(
            name='carreras',
            table='Carreras',
        ),
        migrations.AlterModelTable(
            name='comisiones',
            table='Comisiones',
        ),
        migrations.AlterModelTable(
            name='docentes',
            table='Docentes',
        ),
    ]