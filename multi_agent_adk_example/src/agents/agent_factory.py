from google.adk.agents import Agent
from ..tools.weather_tools import WeatherTools
from ..tools.greeting_tools import GreetingTools
import logging


class AgentFactory:
    """Factory class for creating and configuring agents."""

    def __init__(self):
        """Initialize the AgentFactory."""
        pass

    def get_weather_tools(self):
        """
        Get the weather tools.

        Returns:
            List of weather tools or empty list if failed
        """
        try:
            weather_tools = [WeatherTools().get_weather]
            logging.debug("✅ Weather tools retrieved.")
            return weather_tools
        except Exception as e:
            logging.debug(f"❌ Could not get weather tools. Error: {e}")
            return []

    def get_greeting_tools(self):
        """
        Get the greeting tools.

        Returns:
            List of greeting tools or empty list if failed
        """
        try:
            greeting_tools = [GreetingTools().say_hello]
            logging.debug("✅ Greeting tools retrieved.")
            return greeting_tools
        except Exception as e:
            logging.debug(f"❌ Could not get greeting tools. Error: {e}")
            return []

    def get_farewell_tools(self):
        """
        Get the farewell tools.

        Returns:
            List of farewell tools or empty list if failed
        """
        try:
            farewell_tools = [GreetingTools().say_goodbye]
            logging.debug("✅ Farewell tools retrieved.")
            return farewell_tools
        except Exception as e:
            logging.debug(f"❌ Could not get farewell tools. Error: {e}")
            return []

    def create_greeting_agent(self, model: str):
        """
        Create a greeting agent with the specified configuration.

        Args:
            model: The model to use for the agent

        Returns:
            The created agent instance or None if creation failed
        """
        # Get greeting tools
        greeting_tools = self.get_greeting_tools()

        if greeting_tools:
            try:
                agent = Agent(
                    model=model,
                    name="greeting_agent",
                    instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
                                "Use the 'say_hello' tool to generate the greeting. "
                                "If the user provides their name, make sure to pass it to the tool. "
                                "Do not engage in any other conversation or tasks.",
                    description="Handles simple greetings and hellos using the 'say_hello' tool.",
                    tools=greeting_tools,
                )
                logging.debug(f"✅ Agent '{agent.name}' created using model '{agent.model}'.")
                return agent
            except Exception as e:
                logging.debug(f"❌ Could not create Greeting agent. Check API Key ({model}). Error: {e}")
                return None
        else:
            logging.debug("❌ Cannot create greeting agent because greeting tools are missing.")
            return None

    def create_farewell_agent(self, model: str):
        """
        Create a farewell agent with the specified configuration.

        Args:
            model: The model to use for the agent

        Returns:
            The created agent instance or None if creation failed
        """
        # Get farewell tools
        farewell_tools = self.get_farewell_tools()

        if farewell_tools:
            try:
                agent = Agent(
                    model=model,
                    name="farewell_agent",
                    instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
                                "Use the 'say_goodbye' tool when the user indicates they are leaving or ending the conversation "
                                "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you'). "
                                "Do not perform any other actions.",
                    description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
                    tools=farewell_tools,
                )
                logging.debug(f"✅ Agent '{agent.name}' created using model '{agent.model}'.")
                return agent
            except Exception as e:
                logging.debug(f"❌ Could not create Farewell agent. Check API Key ({model}). Error: {e}")
                return None
        else:
            logging.debug("❌ Cannot create farewell agent because farewell tools are missing.")
            return None

    def create_weather_agent(self, model: str, greeting_agent, farewell_agent):
        """
        Create a weather agent with the specified configuration.

        Args:
            model: The model to use for the agent
            greeting_agent: Instance of GreetingAgent
            farewell_agent: Instance of FarewellAgent

        Returns:
            The created agent instance or None if creation failed
        """
        # Get weather tools
        weather_tools = self.get_weather_tools()

        # Check if sub-agents are available
        greeting_agent_instance = greeting_agent.get_agent() if greeting_agent else None
        farewell_agent_instance = farewell_agent.get_agent() if farewell_agent else None

        if greeting_agent_instance and farewell_agent_instance and weather_tools:
            try:
                agent = Agent(
                    name="weather_agent_v2",
                    model=model,
                    description="The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
                    instruction="You are the main Weather Agent coordinating a team. Your primary responsibility is to provide weather information. "
                                "Use the 'get_weather' tool ONLY for specific weather requests (e.g., 'weather in London'). "
                                "You have specialized sub-agents: "
                                "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                                "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. "
                                "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                                "If it's a weather request, handle it yourself using 'get_weather'. "
                                "For anything else, respond appropriately or state you cannot handle it.",
                    tools=weather_tools,
                    sub_agents=[greeting_agent_instance, farewell_agent_instance]
                )
                logging.debug(f"✅ Root Agent '{agent.name}' created using model '{model}' with sub-agents: {[sa.name for sa in agent.sub_agents]}")
                return agent
            except Exception as e:
                logging.debug(f"❌ Could not create Weather agent. Check API Key ({model}). Error: {e}")
                return None
        else:
            logging.debug("❌ Cannot create root agent because one or more sub-agents failed to initialize or 'get_weather' tool is missing.")
            if not greeting_agent_instance:
                logging.debug(" - Greeting Agent is missing.")
            if not farewell_agent_instance:
                logging.debug(" - Farewell Agent is missing.")
            if not weather_tools:
                logging.debug(" - Weather tools are missing.")
            return None
