import gradio as gr
import subprocess
import os
import signal
import time
import threading
import requests
from pathlib import Path

# Global variable to track the server process
server_process = None

def start_server():
    """Start the Node.js server"""
    global server_process
    try:
        # Kill any existing server
        if server_process:
            server_process.terminate()
            server_process.wait()
        
        # Install dependencies if needed
        if not Path("node_modules").exists():
            print("Installing dependencies...")
            subprocess.run(["npm", "install"], check=True)
        
        # Start the server
        print("Starting SafeGuardLLM server...")
        env = os.environ.copy()
        env["NODE_ENV"] = "production"
        env["PORT"] = "7860"  # Hugging Face Spaces port
        
        server_process = subprocess.Popen(
            ["npm", "run", "start"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to be ready
        max_retries = 30
        for i in range(max_retries):
            try:
                response = requests.get("http://localhost:7860/api/models", timeout=5)
                if response.status_code == 200:
                    print("Server is ready!")
                    return "SafeGuardLLM server started successfully!"
            except:
                pass
            time.sleep(2)
        
        return "Server started but may still be initializing..."
        
    except Exception as e:
        return f"Failed to start server: {str(e)}"

def stop_server():
    """Stop the Node.js server"""
    global server_process
    try:
        if server_process:
            server_process.terminate()
            server_process.wait()
            server_process = None
            return "Server stopped successfully"
        return "No server running"
    except Exception as e:
        return f"Failed to stop server: {str(e)}"

def get_server_status():
    """Check if the server is running"""
    try:
        response = requests.get("http://localhost:7860/api/models", timeout=5)
        if response.status_code == 200:
            return "✅ Server is running"
        else:
            return "❌ Server not responding"
    except:
        return "❌ Server not running"

# Create Gradio interface
with gr.Blocks(title="SafeGuardLLM - Cybersecurity Evaluation Framework") as app:
    gr.Markdown("""
    # SafeGuardLLM - Cybersecurity Evaluation Framework
    
    A comprehensive cybersecurity evaluation framework for systematically assessing Large Language Model vulnerabilities.
    
    ## Features:
    - 2,417+ comprehensive test cases across multiple security domains
    - Multi-provider LLM support (OpenAI, Anthropic, Hugging Face)
    - Real-time evaluation progress tracking
    - Professional security reporting with PDF export
    - Interactive dashboard with security metrics
    
    ## Setup Instructions:
    1. Click "Start Server" below
    2. Add your API keys in the Settings tab of the application
    3. Start evaluating LLM security!
    """)
    
    with gr.Row():
        start_btn = gr.Button("Start Server", variant="primary")
        stop_btn = gr.Button("Stop Server", variant="secondary")
        status_btn = gr.Button("Check Status")
    
    status_output = gr.Textbox(label="Server Status", interactive=False)
    
    gr.Markdown("""
    ### API Keys Required:
    - `OPENAI_API_KEY` - For GPT models
    - `ANTHROPIC_API_KEY` - For Claude models  
    - `HF_TOKEN` - For Hugging Face models
    
    You can set these in the Hugging Face Space settings or in the application interface.
    
    ### Access the Application:
    Once the server is started, you can access the full SafeGuardLLM interface at the URL provided by Hugging Face Spaces.
    """)
    
    # Add an iframe to show the actual application
    gr.HTML("""
    <div style="margin-top: 20px;">
        <h3>SafeGuardLLM Application</h3>
        <iframe src="/" width="100%" height="800" frameborder="0"></iframe>
    </div>
    """)
    
    # Button event handlers
    start_btn.click(start_server, outputs=status_output)
    stop_btn.click(stop_server, outputs=status_output)
    status_btn.click(get_server_status, outputs=status_output)

# Auto-start the server when the Space loads
def auto_start():
    time.sleep(2)  # Give Gradio time to initialize
    start_server()

# Start server in background thread
threading.Thread(target=auto_start, daemon=True).start()

if __name__ == "__main__":
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )