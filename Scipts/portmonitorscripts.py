python script to success mutliple hosts and mutliple ports and provide success or failure results 

example as below 

sit-cc-api-ash-2.a2-v1-ash1-123.host.com 8080 success
sit-cc-api-phx-2.a2-v1-phx1-123.host.com 443 success
sit-cc-api-phx-1.a1-v1-phx1-123.host.com 7000 success
sit-cc-vxml-phx-1.a1-v1-phx1-123.host.com 9050 success
sit-cc-vxml-phx-2.a2-v1-phx1-123.host.com 8081 success
prd-cc-gir-esc-phx-1.a1-v1-phx1-123.host.com 80 success
prd-cc-wwe-esc-phx-4.a2-v1-phx1-123.host.com 9150 success
prd-cc-gir-esc-ash-2.a2-v1-ash1-123.host.com 9200 success
prd-cc-wwe-esc-phx-3.a1-v1-phx1-123.host.com 9200 success
prd-cc-wwe-esc-ash-4.a2-v1-ash1-123.host.com 9300 success
prd-cc-wwe-esc-phx-2.a1-v1-phx1-123.host.com 8082 success
prd-cc-wwe-esc-ash-3.a1-v1-ash1-123.host.com 9200 success
prd-cc-gir-esc-ash-2.a2-v1-ash1-123.host.com 9300 success
prd-cc-wwe-esc-ash-5.a2-v1-ash1-123.host.com 9300 success
prd-cc-gir-esc-ash-1.a1-v1-ash1-123.host.com 9300 success
prd-cc-wwe-api-ash-6.a2-v1-ash1-123.host.com 8080 success
prd-cc-wwe-api-phx-1.a1-v1-phx1-123.host.com 8080 success
prd-cc-scxml-phx-3.a2-v1-phx1-123.host.com 8081 success
prd-cc-scxml-ash-2.a1-v1-ash1-123.host.com 8085 success
prd-cc-scxml-phx-1.a1-v1-phx1-123.host.com 8080 success
prd-cc-scxml-ash-3.a2-v1-ash1-123.host.com 8080 success

#######################

import socket

def check_port(hostname, port):
  """Checks if a port is open on a given hostname.

  Args:
      hostname (str): The hostname of the server.
      port (int): The port number to check.

  Returns:
      str: "success" if the port is open, "failure" otherwise.
  """

  try:
      with socket.create_connection((hostname, port), timeout=5) as sock:
          return "success"
  except (socket.timeout, ConnectionRefusedError, OSError):
      return "failure"

# Sample data (modify with your actual data)
data = [
    ("sit-cc-api-ash-2.a2-v1-ash1-123.host.com", 8080),
    ("sit-cc-api-phx-2.a2-v1-phx1-123.host.com", 443),
    # ... (add more entries here)
    ("prd-cc-scxml-ash-3.a2-v1-ash1-123.host.com", 8080),
]

# Process each data entry
for hostname, port in data:
  result = check_port(hostname, port)
  print(f"{hostname} {port} {result}")
