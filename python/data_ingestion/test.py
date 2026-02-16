import requests
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')


url = "https://api.github.com/repos/DataTalksClub/data-engineering-zoomcamp/events"
url2 =r"https://raw.githubusercontent.com/databricks/Spark-The-Definitive-Guide/refs/heads/master/data/flight-data/csv/2015-summary.csv"
url3 = "https://api.restful-api.dev/objects"
url4 = "https://jsonplaceholder.typicode.com/posts/1"
url5 = "https://httpbin.org/get"

response = requests.get(url=url)

if response.status_code == 200:
    result = response.json()
    print(response.status_code)
    js_data = json.dumps(result,ensure_ascii=False, indent=2)
    print(js_data)

else:
    print(f"Error: {response.status_code}")
