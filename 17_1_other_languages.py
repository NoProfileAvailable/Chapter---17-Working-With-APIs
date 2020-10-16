import requests

# Make an API call on github, to see what are the most popular programming languages
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
# print(f"status code: {r.status_code}")

# JavaScript
url = 'https://api.github.com/search/repositories?q=language:JavaScript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r2 = requests.get(url, headers=headers)
# print(f"status code: {r2.status_code}")

# Ruby
url = 'https://api.github.com/search/repositories?q=language:Ruby&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r3 = requests.get(url, headers=headers)
# print(f"status code: {r3.status_code}")

# C
url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r4 = requests.get(url, headers=headers)
# print(f"status code: {r4.status_code}")

# Perl
url = 'https://api.github.com/search/repositories?q=language:Perl&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r5 = requests.get(url, headers=headers)
# print(f"status code: {r5.status_code}")

# Haskell
url = 'https://api.github.com/search/repositories?q=language:Haskell&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r6 = requests.get(url, headers=headers)

# Go
url = 'https://api.github.com/search/repositories?q=language:Go&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r7 = requests.get(url, headers=headers)

response_dict_java = r.json()
response_dict_javaScript = r2.json()
response_dict_ruby = r3.json()
response_dict_c = r4.json()
response_dict_perl = r5.json()
response_dict_haskell = r6.json()
response_dict_go = r7.json()

# print(response_dict)
print(f"total count Java: {response_dict_java['total_count']}")
print(f"total count JavaScript: {response_dict_javaScript['total_count']}")
print(f"total count Ruby: {response_dict_ruby['total_count']}")
print(f"total count C: {response_dict_c['total_count']}")
# Fehler für die Sprache Perl
#print(f"total count Perl: {response_dict_perl['total_count']}")
print(f"total count Haskell: {response_dict_haskell['total_count']}")
print(f"total count Go: {response_dict_go['total_count']}")


# repo_dicts_java = response_dict['items']
# print(f"items: {len(repo_dicts_java)}")

# repo_dict_java = repo_dicts_java[0]
# print(f"the first item: {len(repo_dict_java)}")


# JAVA
# for repo_dict in repo_dicts_java:
# 	print(f"Repository name: {repo_dict['name']}")
# 	print(f"Repository owner: {repo_dict['owner']['login']}")
# 	print(f"Star: {repo_dict['stargazers_count']}")
# 	print(f"Repository: {repo_dict['html_url']}")
# 	print(f"Created: {repo_dict['created_at']}")
# 	print(f"Updated: {repo_dict['updated_at']}")
# 	print(f"Descripton: {repo_dict['description']}\n")
