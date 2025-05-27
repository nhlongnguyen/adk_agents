# ADK Agents

A multi-agent system built with Google's Agent Development Kit (ADK) for Python.

## Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account with Vertex AI enabled
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

First, clone this repository and navigate to the project directory:

```bash
git clone git@github.com:nhlongnguyen/adk_agents.git
cd adk_agents
```

### 2. Create Python Virtual Environment

First, create and activate a Python virtual environment using `venv`:

```bash
python -m venv .venv
```

Activate the virtual environment using the appropriate command for your operating system:

```bash
# Mac / Linux
source .venv/bin/activate

# Windows CMD:
.venv\Scripts\activate.bat

# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

### 3. Install Google ADK

Install the Google ADK Python package:

```bash
pip install google-adk
```

Verify your installation (optional):

```bash
pip show google-adk
```

For more detailed installation instructions, visit the [official ADK documentation](https://google.github.io/adk-docs/get-started/installation/).

### 4. Set Up Vertex AI Account

1. **Create a Google Cloud Project** (if you don't have one):

   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable Vertex AI API**:

   - In the Google Cloud Console, navigate to APIs & Services > Library
   - Search for "Vertex AI API" and enable it

3. **Set up authentication**:

   - Install the Google Cloud CLI: https://cloud.google.com/sdk/docs/install
   - Run `gcloud auth application-default login` to authenticate
   - Set your project: `gcloud config set project YOUR_PROJECT_ID`

4. **Enable required APIs** (if not already enabled):
   ```bash
   gcloud services enable aiplatform.googleapis.com
   gcloud services enable storage.googleapis.com
   ```

### 5. Configure Environment Variables

1. **Copy the environment template**:

   ```bash
   cp multi_agent_adk_example/.env.example multi_agent_adk_example/.env
   ```

2. **Edit the `.env` file** and set up the following variables:

   ```bash
   # Google Cloud Configuration
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_REGION=us-central1

   # Vertex AI Configuration
   VERTEX_AI_LOCATION=us-central1

   # Additional configuration variables as needed
   # (Add other variables based on your .env.example file)
   ```

   Replace `your-project-id` with your actual Google Cloud project ID.

### 6. Install Additional Dependencies

If there are additional requirements, install them:

```bash
pip install -r requirements.txt
```

## Running the Agent

### Start the Web Server

To test and interact with your agent, start the ADK web server:

```bash
adk web
```

This will start a local web server where you can:

- Test your agents interactively
- View agent responses and behavior
- Debug and monitor agent performance

The web interface will typically be available at `http://localhost:8000` (check the console output for the exact URL).

### Alternative Running Methods

You can also run specific agents directly:

```bash
# Run a specific agent file
python multi_agent_adk_example/agent.py
```

## Project Structure

```
adk_agents/
├── multi_agent_adk_example/
│   ├── src/
│   │   ├── agents/          # Agent implementations
│   │   ├── config/          # Configuration files
│   │   ├── services/        # Service integrations
│   │   └── tools/           # Custom tools
│   ├── agent.py            # Main agent entry point
│   └── .env                # Environment variables (create from .env.example)
├── .venv/                  # Virtual environment
└── README.md              # This file
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**:

   - Ensure you've run `gcloud auth application-default login`
   - Verify your project ID is correct in the `.env` file

2. **API Not Enabled**:

   - Make sure Vertex AI API is enabled in your Google Cloud project
   - Check that billing is enabled for your project

3. **Permission Issues**:

   - Ensure your Google Cloud account has the necessary IAM roles:
     - Vertex AI User
     - Storage Admin (if using Cloud Storage)

4. **Module Import Errors**:
   - Ensure your virtual environment is activated
   - Verify all dependencies are installed with `pip list`

### Getting Help

- [ADK Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Google Cloud Console](https://console.cloud.google.com/)

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
