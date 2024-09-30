import ssl
from ghapi.all import GhApi
import os
import re
import csv
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_ORG = os.getenv('GITHUB_ORG')
TARGET_TEAM_SLUG = os.getenv('TARGET_TEAM_SLUG')  # The team slug for which to list all members and subteams

pattern = re.compile(r".$<FILTER>")

# Bypass SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Initialize GitHub API
api = GhApi(token=GITHUB_TOKEN, owner=GITHUB_ORG)

# Set to store unique members
all_members = set()


# Recursive function to fetch members from a team and its subteams
def get_team_members_and_subteams(org, team_slug):
    # Print the current team slug
    print(f"Processing team: {team_slug}")

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

filtered_members = [member for member in all_members if not pattern.match(member)]

# Convert the set to a list and print unique filtered members
print(filtered_members)

### Export to CSV ###

csv_file = "./get-org-users/filtered_members.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username"])  # Write header
    for member in filtered_members:
        writer.writerow([member])  # Write each member to the CSV

print(f"\nFiltered members have been written to {csv_file}")
