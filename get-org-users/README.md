## Setup Instructions

### 1. Create a `.env` File
In the root of your project (or the parent directory as needed), create a file named `.env`. This file will store your sensitive environment variables such as your GitHub token and organization name.

### 2. Set the `GITHUB_ORG` and `GITHUB_TOKEN`
Inside the `.env` file, add the following lines, replacing the placeholders with your actual values:


- `GITHUB_ORG`: The name of your GitHub organization.
- `GITHUB_TOKEN`: A GitHub Personal Access Token (PAT) with appropriate scopes.
- `TARGET_TEAM_SLUG`: Target team which to loop through

3. Ensure Correct Permissions for `GITHUB_TOKEN`

Make sure the GitHub token has the following permissions (scopes) to allow access to your organization's repositories and teams:

- `read:org`: To read organization and team information.
- `repo`: If you're working with private repositories.
