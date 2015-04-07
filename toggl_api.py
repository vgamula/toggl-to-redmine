import requests


class TogglAPI(object):
    REPORTS_API_VERSION = 'v2'
    REPORTS_API_URL = 'https://www.toggl.com/reports/api/{}'.format(REPORTS_API_VERSION)
    BASE_API_VERSION = 'v8'
    BASE_API_URL = 'https://www.toggl.com/api/{}'.format(BASE_API_VERSION)

    api_token = None

    def __init__(self, api_token):
        self.api_token = api_token

    def _request(self, url, api_url, method="GET", data=None, params=None):
        url = '{api_url}{url}'.format(api_url=api_url, url=url)
        auth = (self.api_token, 'api_token')
        headers = {
            'content-type': 'application/json',
        }
        if method == "POST":
            return requests.post(url, data=data, headers=headers, auth=auth)
        elif method == "GET":
            return requests.get(url, headers=headers, auth=auth, params=params)
        else:
            raise NotImplementedError()

    def _reports_get_request(self, url, params=None):
        return self._request(url=url, method="GET", params=params, data=None, api_url=TogglAPI.REPORTS_API_URL)

    def _base_get_request(self, url, params=None):
        return self._request(url=url, method="GET", params=params, data=None, api_url=TogglAPI.BASE_API_URL)

    def report_summary(self, params=None, data=None):
        resp = self._reports_get_request(url='/summary', params=params)
        return resp.json()

    def me(self):
        return self._base_get_request('/me').json()
