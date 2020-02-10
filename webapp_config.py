import os

#CLIENT_SECRET = "" # Our Quickstart uses this placeholder
# In your production app, we recommend you to use other ways to store your secret,
# such as KeyVault, or environment variable as described in Flask's documentation here
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
if not CLIENT_SECRET:
    raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/langskip.onmicrosoft.com"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

CLIENT_ID = "1aa4529e-0dbd-41e5-b0ed-96e8062a7972"

REDIRECT_PATH = "/getAToken"  # It will be used to form an absolute URL
    # And that absolute URL must match your app's redirect_uri set in AAD

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
#ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
ENDPOINT = 'https://graph.microsoft.com/v1.0/me'

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
#SCOPE = ["User.ReadBasic.All"]
SCOPE = ["User.Read"]

SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session

