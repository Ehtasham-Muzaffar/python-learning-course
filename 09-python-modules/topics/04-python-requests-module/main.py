"""Python requests module: independent learner project. See README.md for purpose and use."""

import requests

request = requests.Request("GET", "https://api.example.invalid", params={"page": 1})
prepared = request.prepare()
print("prepared method and URL:", prepared.method, prepared.url)
print("No network request is made in this lesson; see README.md for safe usage.")
