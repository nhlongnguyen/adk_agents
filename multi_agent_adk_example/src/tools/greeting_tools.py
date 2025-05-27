"""Greeting and farewell tools for the multi-agent system."""

import logging


class GreetingTools:
    """Tools for handling greetings and farewells."""

    @staticmethod
    def say_hello(name: str = "there") -> str:
        """Provides a simple greeting, optionally addressing the user by name.

        Args:
            name (str, optional): The name of the person to greet. Defaults to "there".

        Returns:
            str: A friendly greeting message.
        """
        logging.debug(f"--- Tool: say_hello called with name: {name} ---")
        return f"Hello, {name}!"

    @staticmethod
    def say_goodbye() -> str:
        """Provides a simple farewell message to conclude the conversation."""
        logging.debug(f"--- Tool: say_goodbye called ---")
        return "Goodbye! Have a great day."
