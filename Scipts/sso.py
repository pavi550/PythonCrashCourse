import requests

# Oracle SSO login URL
login_url = "https://elasticsearch-astap.oraclecorp.com/listing"

# Your SSO credentials
username = "elastic"
password = "elastic"

# Session object to persist cookies
session = requests.Session()

# Perform login
login_payload = {
    "username": username,
    "password": password,
    # Additional SSO parameters if required
}

login_response = session.post(login_url, data=login_payload)

# Check if the login was successful (you need to adapt this to Oracle's response)
if "Welcome" in login_response.text:
    print("Login successful!")

# Perform actions on the authenticated session, e.g., access specific pages or resources

# Perform logout (if applicable to Oracle's SSO)
logout_url = "https://www.oracle.com/sso/logout"
logout_response = session.get(logout_url)

# Check if the logout was successful (you need to adapt this to Oracle's response)
if "Logout Successful" in logout_response.text:
    print("Logout successful!")

# Close the session
session.close()
