# Generated by Django 5.1 on 2024-10-16 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_emprestimo_id_ficha_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_prevista',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='motivo_devolução',
            field=models.TextField(),
        ),
    ]
