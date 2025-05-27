from google.adk.agents import Agent
from ..tools.greeting_tools import GreetingTools
import logging

class GreetingAgent:
    """Handles simple greetings and hellos using the 'say_hello' tool."""

    def __init__(self, model: str):
        """
        Initialize the Greeting Agent.

        Args:
            model: The model to use for the agent
            greeting_tools: Instance of GreetingTools containing the say_hello method
        """
        self.model = model
        self.greeting_tools = []
        self.agent = None
        self._get_greeting_tools()
        self._create_agent()

    def _create_agent(self):
        """Create the greeting agent instance."""
        try:
            self.agent = Agent(
                model=self.model,
                name="greeting_agent",
                instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
                            "Use the 'say_hello' tool to generate the greeting. "
                            "If the user provides their name, make sure to pass it to the tool. "
                            "Do not engage in any other conversation or tasks.",
                description="Handles simple greetings and hellos using the 'say_hello' tool.",
                tools=self.greeting_tools,
            )
            logging.debug(f"✅ Agent '{self.agent.name}' created using model '{self.agent.model}'.")
        except Exception as e:
            logging.debug(f"❌ Could not create Greeting agent. Check API Key ({self.model}). Error: {e}")
            self.agent = None

    def _get_greeting_tools(self):
        """Get the greeting tools."""
        try:
            self.greeting_tools = [GreetingTools().say_hello]
            logging.debug(f"✅ Greeting tools retrieved.")
        except Exception as e:
            logging.debug(f"❌ Could not get greeting tools. Error: {e}")
            self.greeting_tools = []

    def get_agent(self):
        """Return the agent instance."""
        return self.agent

    @property
    def name(self):
        """Return the agent name."""
        return self.agent.name if self.agent else None
