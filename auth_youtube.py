import os
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_refresh_token():
    print("جاري فتح المتصفح للحصول على التصريح...")
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    
    print("\n" + "="*50)
    print("✅ تم الربط بنجاح! انسخ الـ Refresh Token ده واحتفظ بيه:")
    print("="*50)
    print(credentials.refresh_token)
    print("="*50 + "\n")

if __name__ == '__main__':
    get_refresh_token()