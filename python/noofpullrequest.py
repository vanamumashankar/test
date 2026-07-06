import requests
url= f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response= requests.get(url)
print(response.status_code)
if response.status_code == 200:
    pull_requests= response.json() #storing all data into dictionary
    pr_creators= {}
    for pull in pull_requests:
        creator= pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
    print("PRs and it cound")
    for creator, count in  pr_creators.items():
        print(f"{creator} has {count} prs")
else:
    print(f"the url status code is {response.status_code}")

