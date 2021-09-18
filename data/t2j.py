import json

filename = 'q1.txt'

result_list = []

with open(filename) as q_f:
    for q in q_f:
        dict1 = {}
        dict1['category']= 'gossip'
        dict1['question']= q.rstrip()
        result_list.append(dict1)

with open('q1.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False, indent=4)