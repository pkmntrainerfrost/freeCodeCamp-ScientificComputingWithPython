def add_time(start, duration, start_day=""):

    duration = [int(i) for i in duration.split(" ")]
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    start_time, start_time_period = [int(i) for i in start.split(" ")[0].split(":")], start.split(" ")[1]


    if start_time_period == "PM":
        start_time += 12

    for day_

    end_time = [0, start_time[i] + end_time[i] for i in range(2)]

    if end_time[2] >= 60:
        end_time[1] += 1
        end_time[2] -= 60

    end_time[0], end_time[1] = end_time[1] // 24, end_time[1] % 24

    return new_time
