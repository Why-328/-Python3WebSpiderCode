import requests

r = requests.get('https://static1.scrape.center/', verify=False)
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
