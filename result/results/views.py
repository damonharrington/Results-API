from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        serial_no = request.POST.get("serial_no")
        dob = request.POST.get("DOB")
        api_url = f'http://127.0.0.1:8000//{serial_no}/{dob}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        clothing_data = response.json()
        if response.status_code == 200:
            clothing_data_data = response.json()
            return render(request, 'results.html', {'clothing_data': clothing_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch clothing details. Check Again!'})
    
        
    return render(request, 'index.html')



