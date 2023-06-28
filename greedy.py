def activity_selector(activities):
    # sort by finish time
    activities.sort(key=lambda x: x[1])
    n = len(activities)
    A = [activities[0]]
    j = 1
    for i in range(1, n):
        if activities[i][0] >= activities[j][1]:
            A.append(activities[i])
            j = i
    return A


activities = [(0, 6), (3, 5), (1, 4), (5, 7), (6, 10), (3, 8),
              (5, 9), (12, 14), (2, 13), (8, 12), (8, 11)]

print(activity_selector(activities))
