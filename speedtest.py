from speedtest import Speedtest

st = Speedtest()

print("your download speed : ", st.download())

print("your upload speed : ", st.upload())

st.get_servers([])
print('ping:', st.results.ping)
