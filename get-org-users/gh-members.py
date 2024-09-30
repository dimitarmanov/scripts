import ssl
from ghapi.all import GhApi
import os
from dotenv import load_dotenv


team_slugs = []
all_members = set()

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_ORG = os.getenv('GITHUB_ORG')

ssl._create_default_https_context = ssl._create_unverified_context

api = GhApi(token=GITHUB_TOKEN, owner=GITHUB_ORG)

teams = api.teams.list(GITHUB_ORG)

team_slugs = [team['slug'] for team in teams]

for team in team_slugs:
    members = api.teams.list_members_in_org(GITHUB_ORG, team)

    for member in members:
        all_members.add(member['login'])

unique_members = list(all_members)
print(unique_members)
