from google.adk.agents import Agent
from ..tools.greeting_tools import GreetingTools
import logging

class FarewellAgent:
    """Handles simple farewells and goodbyes using the 'say_goodbye' tool."""

    def __init__(self, model: str):
        """
        Initialize the Farewell Agent.

        Args:
            model: The model to use for the agent
        """
        self.model = model
        self.farewell_tools = []
        self.agent = None
        self._get_farewell_tools()
        self._create_agent()

    def _create_agent(self):
        """Create the farewell agent instance."""
        try:
            self.agent = Agent(
                model=self.model,
                name="farewell_agent",
                instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
                            "Use the 'say_goodbye' tool when the user indicates they are leaving or ending the conversation "
                            "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you'). "
                            "Do not perform any other actions.",
                description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
                tools=self.farewell_tools,
            )
            logging.debug(f"✅ Agent '{self.agent.name}' created using model '{self.agent.model}'.")
        except Exception as e:
            logging.debug(f"❌ Could not create Farewell agent. Check API Key ({self.model}). Error: {e}")
            self.agent = None

    def _get_farewell_tools(self):
        """Get the farewell tools."""
        try:
            self.farewell_tools = [GreetingTools().say_goodbye]
            logging.debug(f"✅ Farewell tools retrieved.")
        except Exception as e:
            logging.debug(f"❌ Could not get farewell tools. Error: {e}")
            self.farewell_tools = []

    def get_agent(self):
        """Return the agent instance."""
        return self.agent

    @property
    def name(self):
        """Return the agent name."""
        return self.agent.name if self.agent else None
