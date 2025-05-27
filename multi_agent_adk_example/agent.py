# Import necessary libraries
from google.genai import types # For creating message Content/Parts

# Import agent classes
from .src.agents import GreetingAgent, FarewellAgent, WeatherAgent

# Import services for session and runner management
from .src.services import SessionManager, RunnerManager

# Import configuration
from .src.config import AppConfig

import logging
logging.basicConfig(level=logging.INFO)

# Initialize agent instances
greeting_agent = GreetingAgent(AppConfig.MODEL_GEMINI_2_0_FLASH)
farewell_agent = FarewellAgent(AppConfig.MODEL_GEMINI_2_0_FLASH)

# Initialize the main weather agent (now only responsible for agent creation)
weather_agent = WeatherAgent(
    model=AppConfig.MODEL_GEMINI_2_0_FLASH,
    greeting_agent=greeting_agent,
    farewell_agent=farewell_agent
)

# Get the agent instance
root_agent = weather_agent.get_agent()

# Initialize session management
session_manager = SessionManager()
session_manager.create_session(
    app_name=AppConfig.APP_NAME,
    user_id=AppConfig.USER_ID,
    session_id=AppConfig.SESSION_ID
)

# Initialize runner management
runner_manager = RunnerManager()
runner_root = runner_manager.create_runner(
    agent=root_agent,
    app_name=AppConfig.APP_NAME,
    session_service=session_manager.get_session_service()
)
