from .agent_factory import AgentFactory
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

        # Initialize factory
        self.agent_factory = AgentFactory()

        # Initialize agent
        self.agent = None
        self._create_agent()

    def _create_agent(self):
        """Create the farewell agent instance using the factory."""
        self.agent = self.agent_factory.create_farewell_agent(model=self.model)

    def get_agent(self):
        """Return the agent instance."""
        return self.agent

    @property
    def name(self):
        """Return the agent name."""
        return self.agent.name if self.agent else None
