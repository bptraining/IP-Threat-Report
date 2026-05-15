# boot.dev Project 1 - IP Threat Intel Reporter


# VirusTotal IP Scanner

A modular Python Command Line Interface (CLI) tool designed to retrieve and summarize security intelligence for IP addresses using the VirusTotal v3 API.

## 🚀 Features
- **Secure Credential Handling**: Uses `python-dotenv` to keep API keys out of the source code.
- **Modular Architecture**: Separates networking logic, data formatting, and CLI orchestration.
- **Human-Readable Reports**: Converts deep, nested JSON into a clean, summarized terminal output.
- **Time Formatting**: Automatically converts Unix timestamps into readable date-time strings.

## 🛠️ Prerequisites
- Python 3.x
- A VirusTotal API Key ([Get one for free here](https://www.virustotal.com/gui/join-us))

## 📦 Installation

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   # Activate on Mac/Linux:
   source venv/bin/activate
   # Activate on Windows:
   .\venv\Scripts\activate

    Install Dependencies:

    pip install requests python-dotenv

    Configure Environment Variables:
    Create a .env file in the root directory:

    VT_API_KEY=your_virustotal_api_key_here

🖥️ Usage

Run the script by providing an IP address using the -i or --ip flag:

python main.py -i 8.8.8.8

Help Menu

To see all available options and descriptions:

python main.py --help

📂 Project Structure

    main.py: The orchestrator that handles CLI arguments and flow control.
    scanner/api.py: Contains the logic for the HTTP requests to VirusTotal.
    scanner/formatter.py: Handles data transformation, date conversion, and terminal display.
    .env: (Private) Stores sensitive API credentials.
    .gitignore: Ensures the virtual environment and API keys are not committed to version control.

⚖️ License

This project is open-source and available under the MIT License.