import pygeoip

logINFO = open("logs.log", 'a+' )
while True:
	vic_ipad = input("\n\nEnter the Victim's IP address: ")
	logINFO.write("\n%s\n" %(vic_ipad))
	vic_ip = pygeoip.GeoIP("GeoLiteCity.dat")
	llp = vic_ip.record_by_addr(vic_ipad)
	for key, val in llp.items():
		logINFO.write(str(key) + " :  " + str(val) + "\n")
		print('%s : %s' % (key, val))
logINFO.close