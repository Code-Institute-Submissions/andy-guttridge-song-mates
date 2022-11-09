# Generated by Django 3.2.15 on 2022-11-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songmates_main', '0019_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collabrequest',
            name='message',
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre1',
            field=models.CharField(blank=True, choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('BRE', 'Breakcore'), ('CHI', 'Childrens'), ('CHP', 'Chiptune'), ('CLA', 'Classical'), ('COM', 'Comedy'), ('CMM', 'Commercial'), ('COU', 'Country'), ('DAN', 'Dance'), ('DNB', "Drum 'n Bass"), ('DUB', 'Dubstep'), ('EDM', 'EDM'), ('ELE', 'Electronica'), ('FOL', 'Folk'), ('FUS', 'Fusion'), ('HIP', 'Hip Hop'), ('HOU', 'House'), ('IDM', 'IDM'), ('IND', 'Indie'), ('INU', 'Industrial'), ('INS', 'Instrumental'), ('JAZ', 'Jazz'), ('JPO', 'J Pop'), ('JUN', 'Jungle'), ('KPO', 'K Pop'), ('LAT', 'Latin'), ('LOF', 'Lo-fi'), ('MET', 'Metal'), ('NEW', 'New age'), ('OPE', 'Opera'), ('POP', 'Pop'), ('REG', 'Reggae'), ('RNB', 'R & B'), ('ROC', 'Rock'), ('SIN', 'Singer/Songwriter'), ('SND', 'Soundtrack'), ('SOU', 'Soul'), ('SPA', 'Space rock'), ('SPO', 'Spoken word'), ('TEC', 'Techno'), ('TRA', 'Trance'), ('TVT', 'TV Themes'), ('WOR', 'World')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre2',
            field=models.CharField(blank=True, choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('BRE', 'Breakcore'), ('CHI', 'Childrens'), ('CHP', 'Chiptune'), ('CLA', 'Classical'), ('COM', 'Comedy'), ('CMM', 'Commercial'), ('COU', 'Country'), ('DAN', 'Dance'), ('DNB', "Drum 'n Bass"), ('DUB', 'Dubstep'), ('EDM', 'EDM'), ('ELE', 'Electronica'), ('FOL', 'Folk'), ('FUS', 'Fusion'), ('HIP', 'Hip Hop'), ('HOU', 'House'), ('IDM', 'IDM'), ('IND', 'Indie'), ('INU', 'Industrial'), ('INS', 'Instrumental'), ('JAZ', 'Jazz'), ('JPO', 'J Pop'), ('JUN', 'Jungle'), ('KPO', 'K Pop'), ('LAT', 'Latin'), ('LOF', 'Lo-fi'), ('MET', 'Metal'), ('NEW', 'New age'), ('OPE', 'Opera'), ('POP', 'Pop'), ('REG', 'Reggae'), ('RNB', 'R & B'), ('ROC', 'Rock'), ('SIN', 'Singer/Songwriter'), ('SND', 'Soundtrack'), ('SOU', 'Soul'), ('SPA', 'Space rock'), ('SPO', 'Spoken word'), ('TEC', 'Techno'), ('TRA', 'Trance'), ('TVT', 'TV Themes'), ('WOR', 'World')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre3',
            field=models.CharField(blank=True, choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('BRE', 'Breakcore'), ('CHI', 'Childrens'), ('CHP', 'Chiptune'), ('CLA', 'Classical'), ('COM', 'Comedy'), ('CMM', 'Commercial'), ('COU', 'Country'), ('DAN', 'Dance'), ('DNB', "Drum 'n Bass"), ('DUB', 'Dubstep'), ('EDM', 'EDM'), ('ELE', 'Electronica'), ('FOL', 'Folk'), ('FUS', 'Fusion'), ('HIP', 'Hip Hop'), ('HOU', 'House'), ('IDM', 'IDM'), ('IND', 'Indie'), ('INU', 'Industrial'), ('INS', 'Instrumental'), ('JAZ', 'Jazz'), ('JPO', 'J Pop'), ('JUN', 'Jungle'), ('KPO', 'K Pop'), ('LAT', 'Latin'), ('LOF', 'Lo-fi'), ('MET', 'Metal'), ('NEW', 'New age'), ('OPE', 'Opera'), ('POP', 'Pop'), ('REG', 'Reggae'), ('RNB', 'R & B'), ('ROC', 'Rock'), ('SIN', 'Singer/Songwriter'), ('SND', 'Soundtrack'), ('SOU', 'Soul'), ('SPA', 'Space rock'), ('SPO', 'Spoken word'), ('TEC', 'Techno'), ('TRA', 'Trance'), ('TVT', 'TV Themes'), ('WOR', 'World')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre4',
            field=models.CharField(blank=True, choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('BRE', 'Breakcore'), ('CHI', 'Childrens'), ('CHP', 'Chiptune'), ('CLA', 'Classical'), ('COM', 'Comedy'), ('CMM', 'Commercial'), ('COU', 'Country'), ('DAN', 'Dance'), ('DNB', "Drum 'n Bass"), ('DUB', 'Dubstep'), ('EDM', 'EDM'), ('ELE', 'Electronica'), ('FOL', 'Folk'), ('FUS', 'Fusion'), ('HIP', 'Hip Hop'), ('HOU', 'House'), ('IDM', 'IDM'), ('IND', 'Indie'), ('INU', 'Industrial'), ('INS', 'Instrumental'), ('JAZ', 'Jazz'), ('JPO', 'J Pop'), ('JUN', 'Jungle'), ('KPO', 'K Pop'), ('LAT', 'Latin'), ('LOF', 'Lo-fi'), ('MET', 'Metal'), ('NEW', 'New age'), ('OPE', 'Opera'), ('POP', 'Pop'), ('REG', 'Reggae'), ('RNB', 'R & B'), ('ROC', 'Rock'), ('SIN', 'Singer/Songwriter'), ('SND', 'Soundtrack'), ('SOU', 'Soul'), ('SPA', 'Space rock'), ('SPO', 'Spoken word'), ('TEC', 'Techno'), ('TRA', 'Trance'), ('TVT', 'TV Themes'), ('WOR', 'World')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genre5',
            field=models.CharField(blank=True, choices=[('ALT', 'Alternative'), ('BLU', 'Blues'), ('BRE', 'Breakcore'), ('CHI', 'Childrens'), ('CHP', 'Chiptune'), ('CLA', 'Classical'), ('COM', 'Comedy'), ('CMM', 'Commercial'), ('COU', 'Country'), ('DAN', 'Dance'), ('DNB', "Drum 'n Bass"), ('DUB', 'Dubstep'), ('EDM', 'EDM'), ('ELE', 'Electronica'), ('FOL', 'Folk'), ('FUS', 'Fusion'), ('HIP', 'Hip Hop'), ('HOU', 'House'), ('IDM', 'IDM'), ('IND', 'Indie'), ('INU', 'Industrial'), ('INS', 'Instrumental'), ('JAZ', 'Jazz'), ('JPO', 'J Pop'), ('JUN', 'Jungle'), ('KPO', 'K Pop'), ('LAT', 'Latin'), ('LOF', 'Lo-fi'), ('MET', 'Metal'), ('NEW', 'New age'), ('OPE', 'Opera'), ('POP', 'Pop'), ('REG', 'Reggae'), ('RNB', 'R & B'), ('ROC', 'Rock'), ('SIN', 'Singer/Songwriter'), ('SND', 'Soundtrack'), ('SOU', 'Soul'), ('SPA', 'Space rock'), ('SPO', 'Spoken word'), ('TEC', 'Techno'), ('TRA', 'Trance'), ('TVT', 'TV Themes'), ('WOR', 'World')], max_length=3, null=True),
        ),
    ]
