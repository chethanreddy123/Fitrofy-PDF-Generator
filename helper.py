import requests
import json
def fetch_user_details(auth_token):
    url = 'https://app.smartdietplanner.com:8445/api/fetchCustomerDetails'
    headers = {'Authorization': f'Bearer {auth_token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        user_details = response.json()
        return user_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user details: {e}")
        return None



def get_diet_plans(auth_token, date_range, date):
    url = 'https://app.smartdietplanner.com:8445/api/getDietPlans'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "dateRange": date_range,
        "date": date
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        diet_plans = response.json()
        return diet_plans
    except requests.exceptions.RequestException as e:
        print(f"Error fetching diet plans: {e}")
        return None
    
    