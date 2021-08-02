import os
import requests
import sys

from prettytable import PrettyTable
from requests.auth import HTTPBasicAuth


# initialize pretty table with column names
my_table = PrettyTable(["Repo Name", "Stargazers", "Updated time", "Archived", "Size(in KB)"])

# url to query
url = "https://api.github.com/orgs/adobe/repos"

# set this when you want to query next page
get_next_page = True

# generic get request response with basic authentication
# requires env variables "GITHUB_USERNAME" and "GITHUB_TOKEN" to be set


def get_repo_response(url):
    if not url:
        return None
    username = os.getenv("GITHUB_USERNAME", None)
    token = os.getenv("GITHUB_TOKEN", None)
    auth = HTTPBasicAuth(username, token)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    params = {'sort': 'updated', 'per_page': 100, 'direction': 'desc'}
    return requests.get(url=url, headers=headers, params=params, auth=auth)

# retry logic for function 'get_repo_response(url)'
# retry only when http resp code is in [500, 501, 502, 503, 504, 408, 418, 429]
# acceptable response codes are [200, 201]
# raises exception when retries are exhausted
# raises exception when a response code is not in both acceptable&retry lists


def retry_get_repo_response(url):
    retry_if_return_codes = [500, 501, 502, 503, 504] + [408, 418, 429]
    acceptable_return_codes = [200, 201]
    retry_count = 3

    while retry_count >= 0:
        resp = get_repo_response(url)
        if resp.status_code in acceptable_return_codes:
            return resp
        elif resp.status_code in retry_if_return_codes:
            retry_count -= 1
        else:
            raise Exception("Error when hitting url: {}, status: {}, msg: {}".format(
                url, resp.status_code, resp.reason))
    raise Exception("Retry limit exceeded for url: " + url)


# main program logic starts here
try:
    while get_next_page:
        response = retry_get_repo_response(url)

        if not response:
            break

        data = response.json()

        for repo in data:
            my_table.add_row([repo["name"], repo["stargazers_count"], repo["updated_at"], repo["archived"], repo['size']])

        if("next" in response.links):
            get_next_page = True
            url = response.links["next"]["url"]
        else:
            get_next_page = False
            url = None
except Exception as e:
    print("Failed to list repos, " + str(e))
    sys.exit(1)
else:
    print(my_table)
