# Import necessary libraries
from google.genai import types # For creating message Content/Parts

# Import agent classes
from .src.agents import GreetingAgent, FarewellAgent, WeatherAgent

import logging
logging.basicConfig(level=logging.INFO)

# Define the model to use
MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-001"
# Define constants for identifying the interaction context
APP_NAME = "weather_app"
USER_ID = "user_1"
SESSION_ID = "session_001" # Using a fixed ID for simplicity

# Initialize agent instances
greeting_agent = GreetingAgent(MODEL_GEMINI_2_0_FLASH)
farewell_agent = FarewellAgent(MODEL_GEMINI_2_0_FLASH)

# Initialize the main weather agent with sub-agents
weather_agent = WeatherAgent(
    model=MODEL_GEMINI_2_0_FLASH,
    greeting_agent=greeting_agent,
    farewell_agent=farewell_agent,
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

# Get the root agent and runner for backward compatibility
root_agent = weather_agent.get_agent()
runner_root = weather_agent.get_runner()
