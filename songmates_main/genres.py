from django.db import models
from django.utils.translation import gettext_lazy as _


class Genres(models.TextChoices):
    '''
    Defines genres for use in user profile model
    '''
    ALTERNATIVE = 'ALT', _('Alternative'),
    BLUES = 'BLU', _('Blues')
    BREAKCORE = 'BRE', _('Breakcore')
    CHILDRENS = 'CHI', _('Childrens')
    CHIP = 'CHP', _('Chiptune')
    CLASSICAL = 'CLA', _('Classical')
    COMEDY = 'COM', _('Comedy')
    COMMERCIAL = 'CMM', _('Commercial')
    COUNTRY = 'COU', _('Country')
    DANCE = 'DAN', _('Dance')
    DRUM_N_BASS = 'DNB', _("Drum 'n Bass")
    DUBSTEP = 'DUB', _('Dubstep')
    EDM = 'EDM',  _('EDM')
    ELECTRONICA = 'ELE',  _('Electronica')
    FOLK = 'FOL', _('Folk')
    FUSION = 'FUS', _('Fusion')
    HIPHOP = 'HIP', _('Hip Hop')
    HOUSE = 'HOU', _('House')
    IDM = 'IDM', _('IDM')
    INDIE = 'IND', _('Indie')
    INDUSTRIAL = 'INU', _('Industrial')
    INSTRUMENTAL = 'INS', _('Instrumental')
    JAZZ = 'JAZ', _('Jazz')
    J_POP = 'JPO', _('J Pop')
    JUNGLE = 'JUN', _('Jungle')
    K_POP = 'KPO', _('K Pop')
    LATIN = 'LAT', _('Latin')
    LOFI = 'LOF', _('Lo-fi')
    METAL = 'MET', _('Metal')
    NEW = 'NEW', _('New age')
    OPERA = 'OPE', _('Opera')
    POP = 'POP', _('Pop')
    REGGAE = 'REG', _('Reggae')
    RNB = 'RNB', _("R & B")
    ROCK = 'ROC', _('Rock')
    SINGER_SONGWRITER = 'SIN', _('Singer/Songwriter')
    SOUNDTRACK = 'SND', _('Soundtrack')
    SOUL = 'SOU', _('Soul')
    SPACEROCK = 'SPA', _('Space rock')
    SPOKENWORD = 'SPO', _('Spoken word')
    TECHNO = 'TEC', _('Techno')
    TRANCE = 'TRA', _('Trance')
    TV = 'TVT', _('TV Themes')
    WORLD = 'WOR', _('World')
    
