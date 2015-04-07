import json
from datetime import datetime, timedelta

from toggl_api import TogglAPI


def pretty_json(data):
    return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


api = TogglAPI(api_token='5b8a24ee4cc65ddc02b25c71dbab4cd0')


today = datetime.now().replace(hour=0, minute=0, second=0).isoformat()

me = api.me()
my_id = me['data']['id']
user_ids = [my_id]

entries = api.report_summary(params={
    'workspace_id': 729625,
    'user_agent': 'api_test',
    'since': today,
    'user_ids': ','.join([str(x) for x in user_ids]),
    'grouping': 'projects',
    'display_hours': 'decimal'
})

for entry in entries['data']:
    print entry['title']['project']
    for item in entry['items']:
        time = timedelta(milliseconds=item['time'])
        print time
        # print pretty_json(item)
