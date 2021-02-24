import requests
from plotly.graph_objs import Bar
from plotly import offline

# 执行API调用并存储响应。
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

# 处理结果
repo_dicts = response_dict['items']
#repo_names, stars, lables = [], [], []
repo_links, stars, lables = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    lable = f"{owner}<br />{description}"
    lables.append(lable)

# 可视化。
data = [{
    'type': 'bar',
    #'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext': lables,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout ={
    'title': 'Github上最受欢迎的python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '仓库',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '星数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')