# Generated by Django 4.1 on 2022-08-15 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.CharField(max_length=250, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='menu_item',
            field=models.ManyToManyField(to='main_app.menuitem', verbose_name='Related Menu Item(s)'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Recipe Name'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.CharField(max_length=250, verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.CharField(max_length=250, verbose_name='Prep Time'),
        ),
    ]
