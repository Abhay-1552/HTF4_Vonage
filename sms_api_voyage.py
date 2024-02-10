import os
from dotenv import load_dotenv
import vonage

load_dotenv('.env')

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME")
TO_NUMBER = int(os.getenv("TO_NUMBER"))

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

responseData = client.sms.send_message(
    {
        "from": VONAGE_BRAND_NAME,
        "to": TO_NUMBER,
        "text": "A text message sent using the Vonage SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")