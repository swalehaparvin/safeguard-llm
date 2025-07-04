# SafeGuardLLM - Cybersecurity Evaluation Framework

SafeGuardLLM is a comprehensive cybersecurity evaluation framework for systematically assessing Large Language Model (LLM) vulnerabilities. The application provides advanced testing capabilities to assess LLM vulnerabilities across multiple security dimensions including prompt injection, jailbreaking, code interpreter abuse, and data extraction attacks.

#Link to website: https://safeguard-llm.replit.app/

## Features

- **Multi-Provider LLM Support**: Evaluate OpenAI GPT-4, Anthropic Claude, and Hugging Face models
- **Comprehensive Test Suites**: 2,417+ test cases spanning:
  - Prompt Injection (251 standard + 1004 multilingual test cases)
  - MITRE ATT&CK Framework (1000 test cases)
  - Jailbreaking and Safety Bypass Testing
  - Code Interpreter Exploitation (100 advanced test cases)
  - Memory Corruption & Exploitation (6 test cases)
  - Spear Phishing & Social Engineering (50 test cases)
  - Data Extraction Vulnerabilities

- **Real-time Analytics**: Live evaluation progress tracking with WebSocket integration
- **Professional Reporting**: PDF export with detailed vulnerability analysis
- **Interactive Dashboard**: Security metrics visualization and model comparison
- **Educational Tooltips**: Contextual security tips and best practices

## Technology Stack

- **Frontend**: React 18 + TypeScript + Tailwind CSS + shadcn/ui
- **Backend**: Node.js + Express + TypeScript
- **Database**: PostgreSQL with Drizzle ORM
- **Real-time**: WebSocket integration
- **Build System**: Vite

## API Keys Required

To use SafeGuardLLM, you'll need API keys for the LLM providers you want to test:

- `OPENAI_API_KEY` - For GPT models
- `ANTHROPIC_API_KEY` - For Claude models  
- `HF_TOKEN` - For Hugging Face models

## Local Development

1. Clone the repository
2. Install dependencies: `npm install`
3. Set up your environment variables
4. Start the development server: `npm run dev`

## Security Focus

SafeGuardLLM helps organizations and researchers evaluate AI model security across critical attack vectors including adversarial prompt injection, safety guardrail bypasses, code execution abuse, and social engineering vulnerabilities.

## License

MIT License - See LICENSE file for details.
