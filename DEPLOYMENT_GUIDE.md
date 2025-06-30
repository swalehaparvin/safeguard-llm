# SafeGuardLLM - Hugging Face Spaces Deployment Guide

This guide will help you deploy SafeGuardLLM to Hugging Face Spaces.

## Prerequisites

1. A Hugging Face account (free at https://huggingface.co)
2. API keys for the LLM providers you want to test:
   - `OPENAI_API_KEY` - For GPT models
   - `ANTHROPIC_API_KEY` - For Claude models
   - `HF_TOKEN` - For Hugging Face models

## Deployment Steps

### 1. Create a New Hugging Face Space

1. Go to https://huggingface.co/new-space
2. Fill in the details:
   - **Space name**: `safeguard-llm` (or your preferred name)
   - **License**: MIT
   - **SDK**: Gradio
   - **Hardware**: CPU Basic (free tier) or GPU if needed
   - **Visibility**: Public or Private (your choice)

### 2. Upload Your Code

You have two options:

#### Option A: Git Upload (Recommended)
1. Clone your Space repository locally
2. Copy all files from this project to your Space directory
3. Push to your Space repository:
```bash
git add .
git commit -m "Initial SafeGuardLLM deployment"
git push
```

#### Option B: Web Interface Upload
1. In your Space, click "Files" tab
2. Upload all project files:
   - `app.py` (main Gradio interface)
   - `package.json` (Node.js dependencies)
   - `pyproject.toml` (Python dependencies)
   - All `client/`, `server/`, `shared/` directories
   - `Dockerfile`
   - `README.md`
   - Other configuration files

### 3. Configure Environment Variables

1. In your Space settings, go to the "Variables and secrets" section
2. Add your API keys:
   - `OPENAI_API_KEY` (if testing OpenAI models)
   - `ANTHROPIC_API_KEY` (if testing Anthropic models)
   - `HF_TOKEN` (if testing Hugging Face models)

### 4. Space Configuration

Your Space will automatically use the provided `Dockerfile` and configuration files.

## Key Files for Deployment

- **`app.py`**: Main Gradio interface that wraps your Node.js application
- **`Dockerfile`**: Configures the deployment environment
- **`pyproject.toml`**: Python dependencies (Gradio, requests)
- **`package.json`**: Node.js dependencies and build scripts

## How It Works

1. The Gradio interface (`app.py`) provides a simple wrapper
2. It starts your Node.js SafeGuardLLM server in the background
3. Users can access the full application through the embedded iframe
4. The server handles all LLM evaluations and data storage

## Troubleshooting

### Common Issues:

1. **Build Failures**:
   - Ensure all dependencies are properly listed
   - Check that Node.js version is compatible (18+)

2. **API Key Issues**:
   - Verify keys are set in Space settings
   - Check key format and permissions

3. **Memory Issues**:
   - Consider upgrading to a larger Space hardware tier
   - Optimize database queries if needed

4. **Port Conflicts**:
   - The application is configured to use port 7860 (Hugging Face standard)

### Logs and Debugging:

- Check the Space logs in the "Logs" tab
- Monitor both Python (Gradio) and Node.js (SafeGuardLLM) logs
- Use the "Restart Space" button if needed

## Post-Deployment

1. Test the application with a small evaluation
2. Verify all LLM providers work with your API keys
3. Check that evaluations complete successfully
4. Test PDF export functionality

## Space Settings Recommendations

- **Hardware**: CPU Basic for light usage, GPU for heavy evaluation workloads
- **Timeout**: Set to maximum for long-running evaluations
- **Secrets**: Store all API keys securely in Space settings
- **README**: Update with usage instructions for your specific deployment

## Support

If you encounter issues:
1. Check the deployment logs
2. Verify all files were uploaded correctly
3. Ensure API keys are properly configured
4. Test locally first to isolate deployment-specific issues

Your SafeGuardLLM Space will be available at:
`https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`