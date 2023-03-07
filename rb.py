import requests
import geoip2.database

# Get public IP address
ip_response = requests.get('https://api.ipify.org')
ip_address = ip_response.text

# Get country name using GeoIP database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
response = reader.country(ip_address)
country_name = response.country.name

# Align IP address to the left and country name to the right
aligned_ip_address = "{:<20}".format("IP Address: " + ip_address)
aligned_country_name = "{:>20}".format("Country: " + country_name)

# Print the aligned strings
print(aligned_ip_address)
print(aligned_country_name)
