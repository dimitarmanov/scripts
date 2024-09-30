import ssl
from ghapi.all import GhApi
import os
from dotenv import load_dotenv


team_slugs = []
all_members = set()

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_ORG = os.getenv('GITHUB_ORG')
TARGET_TEAM_SLUG = 'customers'

ssl._create_default_https_context = ssl._create_unverified_context

# Initialize GitHub API
api = GhApi(token=GITHUB_TOKEN, owner=GITHUB_ORG)

# Set to store unique members
all_members = set()


# Recursive function to fetch members from a team and its subteams
def get_team_members_and_subteams(org, team_slug):
    print(team_slug)
    # Get members of the current team
    members = api.teams.list_members_in_org(org, team_slug)
    for member in members:
        all_members.add(member['login'])

    # Get subteams of the current team
    subteams = api.teams.list_child_in_org(org, team_slug)
    for subteam in subteams:
        get_team_members_and_subteams(org, subteam['slug'])


# Fetch the main team and its subteams
get_team_members_and_subteams(GITHUB_ORG, TARGET_TEAM_SLUG)

# Convert the set to a list and print unique members
unique_members = list(all_members)
print(unique_members)