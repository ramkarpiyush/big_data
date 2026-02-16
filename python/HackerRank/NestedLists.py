# Problem: Nested Lists

records = [["chi", 20.0], ["beta", 50.0], ["alpha", 55.0], ["delta", 20.0]]

dict = {i[0]:i[1] for i in records}
# print(sorted(dict.values()))

score_set = set()

for i in sorted(dict.values()):
    score_set.add(i)
    
sorted_set_list = list(score_set)

# print(sorted_set_list[1])

res = [i for i,j in dict.items() if j == sorted_set_list[1]]
# print(res)


# Solution2:
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 55.0], ["delta", 20.0]]

records_score_set = set([j for i, j in records])
print(records_score_set)

records_score_set_list = sorted(records_score_set)
print(records_score_set_list)

filter_name = [x for x,y in records if y==records_score_set_list[1]]
print(filter_name)

filter_name = list(
    map(lambda rec: rec[0],                       # take the name
        filter(lambda rec: rec[1] == records_score_set_list[1],      # keep only matching score
               records))
)
print(filter_name)
