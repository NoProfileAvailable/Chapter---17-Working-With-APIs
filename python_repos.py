import requests

# Make an API call and save the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Process results.
#print(response_dict.keys())
print(f"total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"repository returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
# for keys in sorted(repo_dict.keys()):
# 	print(keys)


# Print some information about every the repository
for repo_dict in repo_dicts:
	print(f"Repository name: {repo_dict['name']}")
	print(f"Repository owner: {repo_dict['owner']['login']}")
	print(f"Star: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Descripton: {repo_dict['description']}\n")