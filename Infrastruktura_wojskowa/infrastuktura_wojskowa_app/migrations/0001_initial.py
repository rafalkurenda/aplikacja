# Generated by Django 2.2.7 on 2019-11-14 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulica', models.CharField(max_length=30)),
                ('numer', models.CharField(max_length=30)),
                ('kod_pocztowy', models.CharField(max_length=30)),
                ('miejscowosc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Oddzialy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pododdzial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sprzet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('ilosc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stopien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('wynagrodzenie', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zwiazki_taktyczne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('oddzialy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Oddzialy')),
            ],
        ),
        migrations.CreateModel(
            name='Zwiazki_operacyjne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('zwiazki_taktyczne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Zwiazki_taktyczne')),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('adres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Adres')),
                ('poddodzial', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Pododdzial')),
                ('stopien', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Stopien')),
            ],
        ),
        migrations.AddField(
            model_name='oddzialy',
            name='pododdzial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Pododdzial'),
        ),
        migrations.CreateModel(
            name='Baza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('adres', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Adres')),
                ('sprzet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Sprzet')),
                ('zwiazki_taktyczne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastuktura_wojskowa_app.Zwiazki_taktyczne')),
            ],
        ),
    ]
