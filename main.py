import requests
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + os.environ["AUTH_TOKEN"]
    }
    projects_response = requests.get(get_projects_url(), headers = headers)
    if projects_response is not None and projects_response.status_code == 200:
        projects = projects_response.json()
        for project in projects:
            key_response = requests.get(get_keys_url(project["slug"]), headers = headers)
            if key_response is not None and key_response.status_code == 200:
                keys = key_response.json()
                payload = {
                    "rateLimit" : {
                        "window" : os.environ["RATELIMIT_WINDOW"], # 86400 seconds in a day
                        "count" : os.environ["RATELIMIT_COUNT"]
                    }
                }
                for key in keys:
                    print(f'About to update {project["slug"]}/ key = {key["id"]}')
                    update_response = requests.put(url = get_update_key_url(project["slug"], key["id"]), json = payload, headers = headers)
                    if update_response is not None and update_response.status_code in [200,201]:
                        print("success")
                        print(f'{project["slug"]}/ key = {key["id"]}')
                    else:
                        print("failed")
                        print(update_response.json())


def get_projects_url():
    return f'https://sentry.io/api/0/organizations/{os.environ["ORG_SLUG"]}/projects/'

def get_keys_url(project_slug):
    return f'https://sentry.io/api/0/projects/{os.environ["ORG_SLUG"]}/{project_slug}/keys/'

def get_update_key_url(project_slug, key_id):
    return f'https://sentry.io/api/0/projects/{os.environ["ORG_SLUG"]}/{project_slug}/keys/{key_id}/'

if __name__ == "__main__":
    main()