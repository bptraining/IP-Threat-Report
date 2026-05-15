from datetime import datetime

def format_report(ip, report):
    data = report.get("data", {})
    attributes = data.get("attributes", {})
    stats = attributes.get("last_analysis_stats", {})

    country = attributes.get("country", "unknown")

    # Grab raw timestamp
    raw_date = attributes.get("last_analysis_date", 0)
    
    # Convert to readable date
    readable_date = "Never"
    if raw_date > 0:
        readable_date = datetime.fromtimestamp(raw_date).strftime('%Y-%m-%d %H:%M:%S')

    reputation = attributes.get("reputation", 0)

    harmless = stats.get("harmless", 0)
    malicious = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)

    return {
        "ip": ip,
        "country": country,
        "last_analysis": readable_date,
        "reputation": reputation,
        "harmless": harmless,
        "malicious": malicious,
        "suspicious": suspicious,
    }
    