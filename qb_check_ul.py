import requests
import json
import subprocess

response = requests.get('http://127.0.0.1:8080/api/v2/sync/maindata')
if response.status_code == 200:
    data = response.json()
    alltime_ul = data['server_state']['alltime_ul']
    print(f'Total Traffic Up: {alltime_ul}')
    if alltime_ul > 16*1024*1024*1024*1024:
        subprocess.run(['systemctl', 'stop', 'qbittorrent-nox@admin.service'], check=True);
else:
    print('Failed to retrieve data from qBittorrent')
