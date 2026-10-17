def secondsBetweenTimes(startTime, endTime):
        start_time_arr = startTime.split(":")
        H,M,S = [int(item) for item in start_time_arr]
        H = H*60*60
        M = M*60
        total_start_sec = H+M+S
        End_time_arr = endTime.split(":")
        End_H,End_M,End_S = [int(item) for item in End_time_arr]
        End_H = End_H*60*60
        End_M = End_M*60
        total_end_sec = End_H + End_M + End_S
        return total_end_sec - total_start_sec
