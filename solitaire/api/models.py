from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    SUITS = [
        (1, 'Spades'),
        (2, 'Hearts'),
        (3, 'Diamonds'),
        (4, 'Clubs'),
    ]
    RANKS = [(i, str(i)) for i in range(1, 14)] # 1 - 13 (Ace to King)

    suit = models.IntegerField(choices=SUITS)
    rank = models.IntegerField(choices=RANKS)
    face_up = models.BooleanField(default=False)
    image = models.ImageField()

    def __str__(self):
        return f'{self.get_rank_display()} of {self.get_suit_display()}'
    
class Pile(models.Model):
    PILE_TYPES = [
        ('tableau', 'Tableau'),
        ('foundation', 'Foundation'),
        ('stock', 'Stock'),
        ('waste', 'Waste'),
    ]

    pile_type = models.CharField(max_length=10, choices=PILE_TYPES)
    cards = models.ManyToManyField(Card, related_name='piles')

    def add_card(self, card):
        self.cards.add(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def __str__(self):
        return f'{self.pile_type} Pile'
    
class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tableau_piles = models.ManyToManyField(Pile, related_name='tableau_games')
    foundation_piles = models.ManyToManyField(Pile, related_name='foundation_games')
    stock_pile = models.OneToOneField(Pile, related_name='stock_game', on_delete=models.CASCADE)
    waste_pile = models.OneToOneField(Pile, related_name='waste_game', on_delete=models.CASCADE)
    move_count = models.IntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Game {self.id} for {self.player.username}'
    
class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='moves')
    from_pile = models.ForeignKey(Pile, on_delete=models.CASCADE, related_name='move_from')
    to_pile = models.ForeignKey(Pile, on_delete=models.CASCADE, related_name='move_to')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Move card {self.card} from {self.from_pile} to {self.to_pile}'