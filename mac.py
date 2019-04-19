import http.client

mac1 = input("birinci modemin mac adresini gir\nörnek(c7-k9-74-95-47-9d): ")
print()
mac1sinyal = input(mac1+"'in sinyal kalitesi gir.örnek(-30...-90): ")

mac2 = input("ikinci modemin mac adresini gir\nörnek(c7-k9-74-95-47-9d): ")
print()
mac2sinyal = input(mac2+"'in sinyal kalitesi gir.örnek(-30...-90): ")

conn = http.client.HTTPSConnection("www.googleapis.com")

payload = "{\"wifiAccessPoints\":[{\"age\":0,\"macAddress\":\"%s\",\"signalStrength\":%s},{\"age\":0,\"macAddress\":\"%s\",\"signalStrength\":%s}]}" % (mac1,mac1sinyal,mac2,mac2sinyal)

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

conn.request("POST", "/geolocation/v1/geolocate?key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
