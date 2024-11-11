from django import forms

class PalmistryForm(forms.Form):
    heart_line_choices = [
        ('index', 'Heart Line: Ends at Index Finger'),
        ('middle', 'Heart Line: Ends at Middle Finger'),
        ('both', 'Heart Line: Ends at Middle Finger'),
    ]
    life_line_choices = [
        ('long', 'Life Line: Long'),
        ('short', 'Life Line: Short'),
        ('broken', 'Life Line: Broken'),
    ]
    mind_line_choices = [
        ('straight', 'Mind Line: Straight'),
        ('curve', 'Mind Line: Curve'),
        ('short', 'Mind Line: Short'),
    ]
    fate_line_choices = [
        ('present', 'Fate Line: Present'),
        ('absent', 'Fate Line: Absent'),
        ('broken', 'Fate Line: Broken'),
    ]

    heart_line = forms.ChoiceField(choices=heart_line_choices, widget=forms.RadioSelect)
    life_line = forms.ChoiceField(choices=life_line_choices, widget=forms.RadioSelect)
    mind_line = forms.ChoiceField(choices=mind_line_choices, widget=forms.RadioSelect)
    fate_line = forms.ChoiceField(choices=fate_line_choices, widget=forms.RadioSelect)
