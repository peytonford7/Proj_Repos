# Generated by Django 5.1.1 on 2024-10-11 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.IntegerField(choices=[(1, 'Spades'), (2, 'Hearts'), (3, 'Diamonds'), (4, 'Clubs')])),
                ('rank', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13')])),
                ('face_up', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_count', models.IntegerField(default=0)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pile_type', models.CharField(choices=[('tableau', 'Tableau'), ('foundation', 'Foundation'), ('stock', 'Stock'), ('waste', 'Waste')], max_length=10)),
                ('cards', models.ManyToManyField(related_name='piles', to='api.card')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.card')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='api.game')),
                ('from_pile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='move_from', to='api.pile')),
                ('to_pile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='move_to', to='api.pile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='foundation_piles',
            field=models.ManyToManyField(related_name='foundation_games', to='api.pile'),
        ),
        migrations.AddField(
            model_name='game',
            name='stock_pile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock_game', to='api.pile'),
        ),
        migrations.AddField(
            model_name='game',
            name='tableau_piles',
            field=models.ManyToManyField(related_name='tableau_games', to='api.pile'),
        ),
        migrations.AddField(
            model_name='game',
            name='waste_pile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='waste_game', to='api.pile'),
        ),
    ]
