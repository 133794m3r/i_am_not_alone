import os,csv,time
from ipaddress import IPv4Network,IPv4Address

def main():
	total_lines=172755
	one_percent=total_lines // 100
	i=0;j=0
	file_to_write="/tmpdownload/geo_ip_cleaned-1.csv"
	with open("geoip2-ipv4.csv", "r") as fh,open(file_to_write, "w") as fw:
		writer=csv.writer(fw,delimiter = ',',
			quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
		line=fh.readline()
		writer.writerow(line)
		reader=csv.reader(fh)
		#network, geoname_id, continent_code, continent_name, country_iso_code, country_name, is_anonymous_proxy, is_satellite_provider
		start_time=time.time()
		for network, geoname_id, continent_code, continent_name, country_iso_code, country_name, is_anonymous_proxy, is_satellite_provider in reader:
			i+=1
			#ip_split=network.split('/')
			if network[-2:] == '32':
				start=network[:-3]
				ip=IPv4Address(start)
				start_int=int(ip)
				end=start
				end_int=start_int
			else:
				ips=list(IPv4Network(network).hosts())
				start=str(ips[0])
				start_int=int(ips[0])
				end_int=int(ips[-1])
				end=str(ips[-1])
			tmp_list=[start_int,end_int,start,end,geoname_id,country_iso_code,country_name,continent_name]
			#fw.write('",'.join(tmp_list)+'\n')

			writer.writerow(tmp_list)
			if i >= one_percent:
				cur=time.time()
				delta=cur-start_time
				j+=1
				i=0
				print(f"{j}% done")
				avg = (delta / j)
				eta = avg * (100 - j)
				avg=round(avg,3)
				eta=round(eta,3)
				delta=round(delta,3)
				print(f"So far it's taken {delta}s to complete. And it should take another {eta}s to finish. On average it's taking {avg}s to complete.")

	cur=time.time() - start_time
	print(f"in total it took:{cur}s")

if __name__ == "__main__":
	main()

