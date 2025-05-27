"""
Application configuration constants.
"""

class AppConfig:
    """Configuration class containing application constants."""

    # Model configuration
    MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash-001"

    # Application identification constants
    APP_NAME = "weather_app"
    USER_ID = "user_1"
    SESSION_ID = "session_001"  # Using a fixed ID for simplicity

    @classmethod
    def get_model(cls) -> str:
        """Get the default model name."""
        return cls.MODEL_GEMINI_2_0_FLASH

    @classmethod
    def get_app_name(cls) -> str:
        """Get the application name."""
        return cls.APP_NAME

    @classmethod
    def get_user_id(cls) -> str:
        """Get the user ID."""
        return cls.USER_ID

    @classmethod
    def get_session_id(cls) -> str:
        """Get the session ID."""
        return cls.SESSION_ID
