from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from ..tools.weather_tools import WeatherTools
import logging

class WeatherAgent:
    """The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists."""

    def __init__(self, model: str, greeting_agent, farewell_agent, app_name: str, user_id: str, session_id: str):
        """
        Initialize the Weather Agent.

        Args:
            model: The model to use for the agent
            greeting_agent: Instance of GreetingAgent
            farewell_agent: Instance of FarewellAgent
            app_name: Application name for session management
            user_id: User ID for session management
            session_id: Session ID for session management
        """
        self.model = model
        self.weather_tools = []
        self.greeting_agent = greeting_agent
        self.farewell_agent = farewell_agent
        self.app_name = app_name
        self.user_id = user_id
        self.session_id = session_id

        self.agent = None
        self.session_service = None
        self.session = None
        self.runner = None

        self._get_weather_tools()
        self._create_agent()
        self._setup_session()
        self._create_runner()

    def _get_weather_tools(self):
        """Get the weather tools."""
        try:
            self.weather_tools = [WeatherTools().get_weather]
            logging.debug(f"✅ Weather tools retrieved.")
        except Exception as e:
            logging.debug(f"❌ Could not get weather tools. Error: {e}")
            self.weather_tools = []

    def _create_agent(self):
        """Create the weather agent instance."""
        # Check if sub-agents are available
        greeting_agent_instance = self.greeting_agent.get_agent() if self.greeting_agent else None
        farewell_agent_instance = self.farewell_agent.get_agent() if self.farewell_agent else None

        if greeting_agent_instance and farewell_agent_instance and self.weather_tools:
            try:
                self.agent = Agent(
                    name="weather_agent_v2",
                    model=self.model,
                    description="The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
                    instruction="You are the main Weather Agent coordinating a team. Your primary responsibility is to provide weather information. "
                                "Use the 'get_weather' tool ONLY for specific weather requests (e.g., 'weather in London'). "
                                "You have specialized sub-agents: "
                                "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                                "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. "
                                "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                                "If it's a weather request, handle it yourself using 'get_weather'. "
                                "For anything else, respond appropriately or state you cannot handle it.",
                    tools=self.weather_tools,
                    sub_agents=[greeting_agent_instance, farewell_agent_instance]
                )
                logging.debug(f"✅ Root Agent '{self.agent.name}' created using model '{self.model}' with sub-agents: {[sa.name for sa in self.agent.sub_agents]}")
            except Exception as e:
                logging.debug(f"❌ Could not create Weather agent. Check API Key ({self.model}). Error: {e}")
                self.agent = None
        else:
            logging.debug("❌ Cannot create root agent because one or more sub-agents failed to initialize or 'get_weather' tool is missing.")
            if not greeting_agent_instance:
                logging.debug(" - Greeting Agent is missing.")
            if not farewell_agent_instance:
                logging.debug(" - Farewell Agent is missing.")
            if not self.weather_tools:
                logging.debug(" - Weather tools are missing.")

    def _setup_session(self):
        """Setup the session service and create a session."""
        if self.agent:
            self.session_service = InMemorySessionService()
            self.session = self.session_service.create_session(
                app_name=self.app_name,
                user_id=self.user_id,
                session_id=self.session_id
            )
            logging.info(f"Session created: App='{self.app_name}', User='{self.user_id}', Session='{self.session_id}'")

    def _create_runner(self):
        """Create the runner for the agent."""
        if self.agent and self.session_service:
            self.runner = Runner(
                agent=self.agent,
                app_name=self.app_name,
                session_service=self.session_service
            )
            logging.info(f"Runner created for agent '{self.runner.agent.name}'.")

    def get_agent(self):
        """Return the agent instance."""
        return self.agent

    def get_runner(self):
        """Return the runner instance."""
        return self.runner

    @property
    def name(self):
        """Return the agent name."""
        return self.agent.name if self.agent else None
