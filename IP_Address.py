import re

def is_valid_ip(ip):
    # Regular expression pattern for a valid IPv4 address
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

    # Check if the provided IP address matches the pattern
    if re.match(ip_pattern, ip):
        # Split the IP address into octets
        octets = ip.split('.')
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    else:
        return False

# Test cases
ip1 = "192.168.0.1"
ip2 = "256.0.0.1"

if is_valid_ip(ip1):
    print(f"{ip1} is a valid IP address.")
else:
    print(f"{ip1} is not a valid IP address.")

if is_valid_ip(ip2):
    print(f"{ip2} is a valid IP address.")
else:
    print(f"{ip2} is not a valid IP address.")
