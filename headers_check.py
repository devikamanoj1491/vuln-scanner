import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=5)
        present = []
        missing = []

        for header in SECURITY_HEADERS:
            if header in response.headers:
                present.append(header)
            else:
                missing.append(header)

        return present, missing

    except Exception as e:
        return [], SECURITY_HEADERS
