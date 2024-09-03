# Generated by Django 5.0.1 on 2024-01-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameresponse',
            name='difficulty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gameresponse',
            name='expected_response',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gameresponse',
            name='response',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gameresponse',
            name='is_correct',
            field=models.BooleanField(null=True),
        ),
    ]