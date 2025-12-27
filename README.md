# AI Code Assistant Agent

An intelligent Python agent that leverages Google's Gemini API to autonomously perform coding tasks. The agent can read files, execute Python scripts, and write new files while maintaining context through multi-turn conversations.

## Features

- **Agentic Loop**: Implements a multi-turn conversation with the Gemini API (up to 8 iterations)
- **Tool Integration**: The agent has access to four core tools:
  - List files and directories
  - Read file contents
  - Execute Python files with optional arguments
  - Write or overwrite files
- **Context Management**: Maintains full conversation history to enable the model to make informed decisions
- **Error Handling**: Includes try/except blocks and validation checks
- **Verbose Mode**: Optional detailed logging of API calls and function executions

## Requirements

- Python 3.13 or higher
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_Agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or with pip directly:
```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

3. Set up your environment variables:
Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the agent with a prompt:

```bash
python main.py "Your prompt here"
```

Enable verbose output to see detailed information about API calls and function executions:

```bash
python main.py "Your prompt here" --verbose
```

### Examples

```bash
python main.py "List all files in the calculator directory"
python main.py "Read the calculator/main.py file" --verbose
python main.py "Run the tests in calculator/tests.py"
```

## Project Structure

```
.
├── main.py                 # Entry point and main agent loop
├── call_function.py        # Function execution dispatcher
├── prompts.py             # System prompt for the agent
├── config.py              # Configuration constants
├── functions/             # Tool implementations
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/            # Example working directory
├── pyproject.toml         # Project metadata
└── README.md             # This file
```

## How It Works

1. User provides a prompt via command line
2. Agent makes an API call to Gemini 2.5 Flash with the prompt
3. If the model requests tool calls:
   - Each function is executed with the provided arguments
   - Results are formatted and sent back to the model
   - The conversation continues (agentic loop)
4. When the model provides a final response without function calls, it is displayed to the user
5. Loop terminates after a maximum of 8 iterations to prevent infinite loops

## Configuration

Edit `config.py` to adjust:
- `WORKING_DIR`: The base directory for file operations (default: `./calculator`)
- `MAX_CHARS`: Character limit for file content (default: `10000`)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request.
