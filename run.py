import pygeoip

GEO_LITE_CITY = "GeoLiteCity/GeoLiteCity.dat"


def get_position(ip_address: str):
    raw_data = pygeoip.GeoIP(GEO_LITE_CITY)
    data_map = raw_data.record_by_addr(ip_address)
    latitude = data_map['latitude']
    longitude = data_map['longitude']
    if longitude >= 0:
        polarity = "+"
    else:
        polarity = "-"
    earth_url = "https://earth.google.com/web/search/{},{}{}/".format(latitude, polarity, longitude)
    return earth_url


if __name__ == "__main__":
    victim_ip_address = input("\n\n[+] Enter the Victim's IP address: ")
    position = get_position(victim_ip_address)
    print("Position: {}".format(position))
