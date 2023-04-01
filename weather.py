import requests

url = "http://api.qingyunke.com/api.php?key=free&msg=温州天气"


response = requests.request("GET", url)

data = response.text
start = data.find("content") + 10
end = data.find("}") - 1
answer = data[start:end]

print(answer)
