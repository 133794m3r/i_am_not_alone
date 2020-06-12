import os,csv
from ipaddress import IPv4Network

def main():
	with open("geoip2-ipv4.csv","r") as fh,open("/tmpdownload/geo_ip_cleaned.csv","w") as fw:
		writer=csv.writer(fw,delimiter = ',',
			quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
		fh.readline()
		reader=csv.reader(fh)
		#network, geoname_id, continent_code, continent_name, country_iso_code, country_name, is_anonymous_proxy, is_satellite_provider
		for network, geoname_id, continent_code, continent_name, country_iso_code, country_name, is_anonymous_proxy, is_satellite_provider in reader:
			ip_split=network.split('/')
			if ip_split[1] == '32':
				start=ip_split[0]
				end=ip_split[1]
			else:
				ips=list(IPv4Network(network).hosts())
				start=str(ips[0])
				end=str(ips[-1])
			tmp_list=[start,end,geoname_id,country_iso_code,country_name,continent_name]
			#fw.write('",'.join(tmp_list)+'\n')

			writer.writerow(tmp_list)


if __name__ == "__main__":
	main()

