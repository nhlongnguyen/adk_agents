from google.adk.sessions import InMemorySessionService
import logging


class SessionManager:
    """Manages session creation and lifecycle for agents."""

    def __init__(self):
        """Initialize the SessionManager."""
        self.session_service = None
        self.session = None

    def create_session_service(self):
        """Create and return a session service."""
        if not self.session_service:
            self.session_service = InMemorySessionService()
            logging.debug("✅ Session service created.")
        return self.session_service

    def create_session(self, app_name: str, user_id: str, session_id: str):
        """
        Create a session with the given parameters.

        Args:
            app_name: Application name for session management
            user_id: User ID for session management
            session_id: Session ID for session management

        Returns:
            The created session
        """
        if not self.session_service:
            self.create_session_service()

        self.session = self.session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            session_id=session_id
        )
        logging.info(f"Session created: App='{app_name}', User='{user_id}', Session='{session_id}'")
        return self.session

    def get_session_service(self):
        """Return the session service instance."""
        return self.session_service

    def get_session(self):
        """Return the session instance."""
        return self.session
