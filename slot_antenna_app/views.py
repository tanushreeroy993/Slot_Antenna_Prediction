from django.shortcuts import render
from .forms import AntennaForm
import joblib
import numpy as np
import os
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'model', 'multi_output_rf_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'model', 'scaler.pkl'))

@login_required
def predict_view(request):
    output_labels = [
        'Bandwidth (%)',
        'Radiation Efficiency (%)', 
        'Total Efficiency (%)', 
        'Gain (dBi)',
        'F/B Ratio'
    ]
    
    prediction = None
    if request.method == 'POST':
        form = AntennaForm(request.POST)
        # Always use the POST data form instance, regardless of validation
        if form.is_valid():
            try:
                # Ensure l3/l4 fields are set to 0 if not provided (for 2-loop case)
                if form.cleaned_data.get('number_of_loop') == '2':
                    for field in ['l3_outer', 'l3_inner', 'l4_outer', 'l4_inner']:
                        form.cleaned_data[field] = 0.0
                else:
                    for field in ['l3_outer', 'l3_inner', 'l4_outer', 'l4_inner']:
                        if not form.cleaned_data.get(field):
                            form.cleaned_data[field] = 0.0
                # Prepare input data
                input_data = np.array([[form.cleaned_data[field] for field in form.fields]])
                
                # Scale and predict
                input_scaled = scaler.transform(input_data)
                predicted_values = model.predict(input_scaled)[0].tolist()
                
                # Pair labels with values
                prediction = list(zip(output_labels, predicted_values))
                
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
    else:
        form = AntennaForm()  # Only create a new form for GET requests

    return render(request, 'slot_antenna_app/index.html', {
        'form': form,
        'prediction': prediction
    })