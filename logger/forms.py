from django.forms import ModelForm, ModelChoiceField
from dal import autocomplete

from logger.models import Match, God


class MatchForm(ModelForm):
    # god = ModelChoiceField(
    #     queryset=God.objects.all(),
    #     widget=autocomplete.ModelSelect2(
    #         url='god-autocomplete',
    #         attrs={'data-placeholder': 'God name'}
    #     ),
    #     required=False
    # )
    # self = god
    # opponent = god

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
        widgets = {
            'self': autocomplete.ModelSelect2(url='god-autocomplete'),
            'opponent': autocomplete.ModelSelect2(url='god-autocomplete')
        }
