import os
from dotenv import load_dotenv
import vonage


class API:
    def __init__(self):
        load_dotenv('.env')

        self.VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
        self.VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
        self.VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME")
        self.TO_NUMBER = int(os.getenv("TO_NUMBER"))

    def send_sms(self, name, mail, data):
        client = vonage.Client(key=self.VONAGE_API_KEY, secret=self.VONAGE_API_SECRET)

        responsedata = client.sms.send_message(
            {
                "from": self.VONAGE_BRAND_NAME,
                "to": self.TO_NUMBER,
                "text": f"{name} <{mail}>\n{data}",
            }
        )

        if responsedata["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responsedata['messages'][0]['error-text']}")
