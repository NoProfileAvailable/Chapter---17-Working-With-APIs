from operator import itemgetter
import json
import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"status code: {r.status_code}")


submission_ids = r.json()
submission_dicts = []

comments, informations = [], []

for submission_id in submission_ids[:15]:
	try:
		url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
		r = requests.get(url)
		#print(f"status code: {r.status_code}")

		repo_dict = r.json()

		repo_name = repo_dict['by']
		repo_title= repo_dict['title']
		information = f"<a href='{repo_name}'>{repo_title}</a>"
		informations.append(information)

		repo_comments = repo_dict['descendants']


		comments.append(repo_comments)
	except KeyError:
		repo_comments = 0
		comments.append(repo_comments)

comments = sorted(comments, reverse=True)


data = [{
	'type': 'bar',
	'x': informations,
	'y': comments,
	'hovertext': informations,

}]

my_layout = {
	'title': 'Most commented articles',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 18},
		'tickfont': {'size': 8},
		},
	'yaxis': {
		'title': 'Comments',
		'titlefont': {'size': 18},
		'tickfont': {'size':8},
		},
}

fig= {'data': data, 'layout': my_layout}
offline.plot(fig, filename='17_2_active_discussions.html')



# 	submission_dict = {
# 		'title': repo_dict['title'],
# 		'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
# 		'comments': repo_dict['descendants']
# 	}

# 	submission_dicts.append(submission_dict)

# submission_dicts = sorted(submission_dicts, key=itemgetter('comments') ,reverse = True)

# for submission_dict in submission_dicts:
# 		print(f"\nTitle: {submission_dict['title']}")
# 		print(f"Discussion link: {submission_dict['hn_link']}")
# 		print(f"Comments: {submission_dict['comments']}")