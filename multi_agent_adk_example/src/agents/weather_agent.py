from .agent_factory import AgentFactory
import logging


class WeatherAgent:
    """The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists."""

    def __init__(self, model: str, greeting_agent, farewell_agent):
        """
        Initialize the Weather Agent.

        Args:
            model: The model to use for the agent
            greeting_agent: Instance of GreetingAgent
            farewell_agent: Instance of FarewellAgent
        """
        self.model = model
        self.greeting_agent = greeting_agent
        self.farewell_agent = farewell_agent

        # Initialize factory
        self.agent_factory = AgentFactory()

        # Initialize agent
        self.agent = None
        self._create_agent()

    def _create_agent(self):
        """Create the weather agent instance using the factory."""
        self.agent = self.agent_factory.create_weather_agent(
            model=self.model,
            greeting_agent=self.greeting_agent,
            farewell_agent=self.farewell_agent
        )

    def get_agent(self):
        """Return the agent instance."""
        return self.agent

    @property
    def name(self):
        """Return the agent name."""
        return self.agent.name if self.agent else None
