from google.adk.runners import Runner
import logging


class RunnerManager:
    """Manages runner creation and lifecycle for agents."""

    def __init__(self):
        """Initialize the RunnerManager."""
        self.runner = None

    def create_runner(self, agent, app_name: str, session_service):
        """
        Create a runner for the given agent.

        Args:
            agent: The agent instance to create a runner for
            app_name: Application name for the runner
            session_service: The session service to use

        Returns:
            The created runner instance
        """
        if not agent:
            logging.error("❌ Cannot create runner: agent is None")
            return None

        if not session_service:
            logging.error("❌ Cannot create runner: session_service is None")
            return None

        try:
            self.runner = Runner(
                agent=agent,
                app_name=app_name,
                session_service=session_service
            )
            logging.info(f"Runner created for agent '{agent.name}'.")
            return self.runner
        except Exception as e:
            logging.error(f"❌ Failed to create runner: {e}")
            return None

    def get_runner(self):
        """Return the runner instance."""
        return self.runner
