class TopVotedCandidate:

    def __init__(self, persons, times):
        self.persons = persons
        self.times = times

        self.lead = []

        self.dict = {}

        for i in range(len(persons)):
            if i == 0:
                self.lead.append(persons[i])
                self.dict[persons[i]] = 1

            else:
                if persons[i] not in self.dict:
                    self.dict[persons[i]] = 1

                else:
                    self.dict[persons[i]] += 1

                if self.dict[persons[i]] >= self.dict[self.lead[-1]]:
                    self.lead.append(persons[i])
                else:
                    self.lead.append(self.lead[-1])

        #print(self.lead)


    def q(self, t: int) -> int:

        def bisect_left(times,t):

            l,r =0, len(times)-1

            while l < r:
                mid = (l+r)//2

                if times[mid] < t:
                    l  = mid + 1
                else:
                    r = mid

            return l

        ans = bisect_left(self.times,t)

        if self.times[ans] == t:
            return self.lead[ans]
        elif t > self.times[-1]:
            return self.lead[-1]
        else:
            return self.lead[ans-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
