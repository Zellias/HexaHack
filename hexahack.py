import requests
import os

# Base URL for the HexaCore API
base_url = "https://hexacore-tg-api.onrender.com/api"

# Clear the console for better readability of the output
os.system('cls' if os.name == 'nt' else 'clear')

def get_token(username: str, user_id: int):
    """
    Obtain an authorization token for a given user.
    
    Parameters:
        username (str): The username of the user.
        user_id (int): The unique identifier for the user.
        
    Returns:
        str: An authorization token.
    """
    response = requests.post(
        f"{base_url}/app-auth", json={"user_id": user_id, "username": username}
    )
    return response.json()["token"]

def create_account(user_id: int, fullname: str, username: str, referer_id: int):
    """
    Create a new user account in the system.
    
    Parameters:
        user_id (int): The unique identifier for the user.
        fullname (str): The full name of the user.
        username (str): The username for the user.
        referer_id (int): The unique identifier of the referer.
        
    Returns:
        bool: True if account creation was successful, False otherwise.
    """
    response = requests.post(
        f"{base_url}/create-user",
        json={
            "user_id": user_id,
            "fullname": fullname,
            "username": username,
            "referer_id": referer_id,
        },
        headers={"Authorization": f"{get_token(username, user_id)}"},
    )
    return response.json()["success"]

def available_taps(username: str, user_id: int):
    """
    Retrieve the number of available taps for a user.
    
    Parameters:
        username (str): The username of the user.
        user_id (int): The unique identifier for the user.
        
    Returns:
        int: The number of available taps.
    """
    response = requests.get(
        f"{base_url}/available-taps",
        headers={"Authorization": f"{get_token(username, user_id)}"},
    )
    return response.json()["available_taps"]

def mineall(username: str, user_id: int):
    """
    Execute mining for all available taps for a user.
    
    Parameters:
        username (str): The username of the user.
        user_id (int): The unique identifier for the user.
        
    Returns:
        bool: True if mining was successful, False otherwise.
    """
    response = requests.get(
        f"{base_url}/mining-complete",
        data={"taps": available_taps(username, user_id)},
        headers={"Authorization": f"{get_token(username, user_id)}"},
    )
    return response.json()["success"]

def get_balance(username: str, user_id: int):
    """
    Retrieve the balance of a user.
    
    Parameters:
        username (str): The username of the user.
        user_id (int): The unique identifier for the user.
        
    Returns:
        float: The current balance of the user.
    """
    response = requests.get(
        f"{base_url}/balance/{user_id}",
        headers={"Authorization": f"{get_token(username, user_id)}"},
    )
    return response.json()["balance"]

