from django.forms import ModelForm

from logger.models import Match


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = [
            'self',
            'opponent',
            'result',
            'date',
            'kills',
            'deaths',
            'notes',
        ]
