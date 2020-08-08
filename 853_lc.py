class Solution:
    def carFleet(self, target: int, position, speed):
        if len(position) == 0:
            return 0
        else:
            # build a map with car:speed
            dic = {}
            for i in range(len(speed)):
                dic[position[i]] = speed[i]

            position.sort()
            fleet_cnt = 0
            time = []
            for i in range(len(position)):
                time.append((target-position[i])/dic[position[i]])
            #time = [12.0, 3.0, 7.0, 1.0, 1.0]

            j = len(time)-1
            thres = 0
            while j >= 0:
                if thres == 0:
                    thres = time[j]
                    j -= 1
                    fleet_cnt += 1
                    continue
                else:
                    if time[j] > thres:
                        fleet_cnt+=1
                        thres = time[j]
                        j -= 1
                    else:
                        j -= 1

            return fleet_cnt
