from langchain.tools import BaseTool, Tool, tool
import os
from twilio.rest import Client

class TwilioSendMessage(BaseTool):
    name = "TwilioSendMessage"
    description = """
        This tool sends an SMS message using the Twilio API.
        Input to this tool will be the message body and the recipient's phone number.
        Example input: 'Hello from Langchain!', '+1234567890'
    """

    def _run(
        self,
        input: str
    ):
        message_body, recipient_number = [each.strip() for each in input.split(",")]
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message_body,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),  # Your Twilio phone number
            to=recipient_number  # Recipient's phone number
        )

        return f"Message sent successfully! SID: {message.sid}"

twilio_send_message_tool = Tool(
    name=TwilioSendMessage().name,
    description=TwilioSendMessage().description,
    func=TwilioSendMessage().run
)