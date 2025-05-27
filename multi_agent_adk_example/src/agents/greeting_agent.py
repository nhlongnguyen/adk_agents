from .agent_factory import AgentFactory
import logging


class GreetingAgent:
    """Handles simple greetings and hellos using the 'say_hello' tool."""

    def __init__(self, model: str):
        """
        Initialize the Greeting Agent.

        Args:
            model: The model to use for the agent
        """
        self.model = model

        # Initialize factory
        self.agent_factory = AgentFactory()

        # Initialize agent
        self.agent = None
        self._create_agent()

    def _create_agent(self):
        """Create the greeting agent instance using the factory."""
        self.agent = self.agent_factory.create_greeting_agent(model=self.model)

    def get_agent(self):
        """Return the agent instance."""
        return self.agent

    @property
    def name(self):
        """Return the agent name."""
        return self.agent.name if self.agent else None
