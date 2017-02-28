# coding:utf-8
"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution(object):
    def reconstructQueue(self, people):
        if not people:
            return []
        people_dict, height, result = {}, [], []
        for i,v in enumerate(people):
            if v[0] not in people_dict:
                people_dict[v[0]] = [(v[1],i)]
                height.append(v[0])
            else:
                people_dict[v[0]].append((v[1],i))
        height.sort(reverse=True)
        for h in height:
            for g in sorted(people_dict[h]):
                result.insert(g[0],people[g[1]])
        return result

