# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print("Server Name: ", server_name)
print("Port: ", port)
print("htTPS Enabled:", is_https_enabled)
print("Max Connections:", max_connections)

# Update configuration values
port = 443
is_https_enabled = False

# Print the updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")