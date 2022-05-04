import pygeoip

GEO_LITE_CITY = "GeoLiteCity/GeoLiteCity.dat"


def get_position(ip_address: str):
    raw_data = pygeoip.GeoIP(GEO_LITE_CITY)
    data_map = raw_data.record_by_addr(ip_address)
    lat_long = "{}, {}".format(data_map['latitude'], data_map['longitude'])
    return lat_long


if __name__ == "__main__":
    victim_ip_address = input("\n\n[+] Enter the Victim's IP address: ")
    position = get_position(victim_ip_address)
    print("Position: {}".format(position))
