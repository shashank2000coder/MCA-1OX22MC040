import requests

# Replace with your actual access code
access_code = "your_access_code"

# Make API call with authentication
def fetch_train_data():
    headers = {"Authorization": f"Bearer {access_code}"}
    response = requests.get("https://api.johndoerailways.com/trains", headers=headers)
    return response.json()
from django.http import JsonResponse

def get_sorted_trains(request):
    train_data = fetch_train_data()
    sorted_trains = sort_trains(train_data)
    return JsonResponse({"trains": sorted_trains})