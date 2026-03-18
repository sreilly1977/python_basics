line = "Failed login from 192.168.1.50 user=admin"

parts = line.split()
ip = parts[3]
user = line.split("user=")[1]

print("IP:", ip)
print("User:", user)
