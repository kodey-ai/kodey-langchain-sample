import os
import sys
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools.twilio import twilio_send_message_tool

# Load environment variables
load_dotenv()

# Define the OpenAI Chat LLM instance
llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=0)

# Initialize the Langchain agent with the Twilio tool
agent = initialize_agent(
    tools=[twilio_send_message_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# Accept input from the user via command line arguments
user_input = ' '.join(sys.argv[1:])

# Invoke the agent with the user input
response = agent.invoke({"input": user_input})
print(response)