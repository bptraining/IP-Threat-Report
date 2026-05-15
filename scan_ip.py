import argparse
import os #reads the .env
from dotenv import load_dotenv #sets the .env

# Import VirusTotal IP api call
from scanner.api import scan_ip
# Import formatter
from scanner.formatter import format_report, print_summary

# Load env variables from .env
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="VirusTotal IP Scanner")
    parser.add_argument("-i", "--ip", help="Scan a single IP address")
    #parser.add_argument("-f", "--file", help="Scan a list of IPs from a text file")

    args = parser.parse_args()

    api_key = os.getenv("VT_API_KEY")

    if not api_key:
        print("ERROR: No API key found in environment.")
        return
    
    test_ip = "8.8.8.8" # Google DNS
    # Single IP mode
    if args.ip:
        try:
            scan = scan_ip(api_key, args.ip)
            summary = format_report(args.ip, scan)
            print_summary(summary)

        except Exception as e:
            print(f"An error occured: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()