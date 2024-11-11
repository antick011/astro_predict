from django.shortcuts import render
from .forms import PalmistryForm

def predict(request):
    prediction = None

    if request.method == 'POST':
        form = PalmistryForm(request.POST)
        if form.is_valid():
            # Get form data
            heart_line = form.cleaned_data['heart_line']
            life_line = form.cleaned_data['life_line']
            mind_line = form.cleaned_data['mind_line']
            fate_line = form.cleaned_data['fate_line']

            # Prediction logic
            predictions = {
                'heart_line': {
                    'index': 'Emotionally balanced',
                    'middle': 'Passionate, Intense personality',
                    'both': 'Compassionate, Empathetic',
                },
                'life_line': {
                    'long': 'Healthy life',
                    'short': 'Need care',
                    'broken': 'Average',
                },
                'mind_line': {
                    'straight': 'Analytical',
                    'curve': 'Creative',
                    'short': 'Technical',
                },
                'fate_line': {
                    'present': 'Smart work',
                    'absent': 'Hard work',
                    'broken': 'Change present work style',
                }
            }

            # Generate the result based on the input
            prediction = {
                'heart_line': predictions['heart_line'][heart_line],
                'life_line': predictions['life_line'][life_line],
                'mind_line': predictions['mind_line'][mind_line],
                'fate_line': predictions['fate_line'][fate_line],
            }

    else:
        form = PalmistryForm()

    return render(request, 'predictor/index.html', {'form': form, 'prediction': prediction})