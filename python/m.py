my= { 'test1': 'uma', 'test2': 26, 'test3': 30 }
addd=my['test4'] = 'e'
modi=my['test1'] = 'test1'
del my['test3']
print("---------------------------------",addd)
print("----------",modi)
print("--------------",my.items())
for i, j in my.items():
    print(i,":", j)
    print(my['test2'])


my_set={1,2,3,5}
print(my_set)
my_set.add(4)
print(my_set)
my_set.remove(5)
print(my_set)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set = set1.difference(set2)
difference_set1 = set2.difference(set1)  # Difference of sets
print(union_set)
print(intersection_set)
print(difference_set)
print(difference_set1)
is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2
print(is_subset)
print(is_superset)
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
server_name= input("enter server: ")
def get_status(server_name):
      return server_config.get(server_name, {}).get('status','Not found')
status= get_status(server_name)
print(f"{server_name} status is {status}")