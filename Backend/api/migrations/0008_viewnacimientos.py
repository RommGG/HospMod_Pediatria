# Generated by Django 4.1.13 on 2024-04-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_viewnacimientos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewNacimientos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pn_masculino', models.IntegerField(null=True)),
                ('pn_femeninos', models.IntegerField(null=True)),
                ('c_masculino', models.IntegerField(null=True)),
                ('c_femenino', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'vw_nacimientos_genero',
                'managed': False,
            },
        ),
    ]
