from ports_scan import scan_ports
from headers_check import check_security_headers

if __name__ == "__main__":
    target_url = "https://google.com"
    host = "google.com"

    ports = scan_ports(host)
    present, missing = check_security_headers(target_url)

    print("Open ports:", ports)
    print("Security headers present:", present)
    print("Security headers missing:", missing)
