import requests
import base64
import pandas as pd
from io import StringIO

# GitHub API URL to the file
api_url = "https://api.github.com/repos/databricks/Spark-The-Definitive-Guide/contents/data/retail-data/by-day/2010-12-01.csv"

# Make request
response = requests.get(api_url)
response.raise_for_status()  # Raise error if request failed

# Decode base64 content
file_content = base64.b64decode(response.json()['content']).decode('utf-8')

# Read into DataFrame
df = pd.read_csv(StringIO(file_content))

# Show result
print(df.head())
