from django import forms
from .models import Review


class Add_ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ('title', 'rating', 'body',)

    rating = forms.Select(
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        )
    )
