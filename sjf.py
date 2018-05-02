# shortest job first
n = input("enter the number of processes: ")
print n

burst_time = [0]*n
process = [0]*n
arrival_time = [0]*n

for c1 in range(n):
    burst_time[c1] = input("enter burst time: ")

    process[c1] = input("enter process number:")
print "burst time of processes:"

for c1 in range(n):
    print burst_time[c1]

for c1 in range(n):
    for c2 in range(n-1):

        if burst_time[c2] > burst_time[c2+1]:

            temp1 = burst_time[c2]
            burst_time[c2] = burst_time[c2+1]
            burst_time[c2+1] = temp1

            temp2 = process[c2]
            process[c2] = process[c2 + 1]
            process[c2 + 1] = temp2
print "Process   burst time   waiting time   turnaround time"
for c1 in range(n):
    if c1 == 0:
        print "P", process[c1], "      ", burst_time[c1], "          ", 0, "           ", burst_time[c1] - arrival_time[c1]

    elif c1 > 0:
        waiting_time = 0
        waiting_time2 = 0
        for c2 in range(c1):
            waiting_time += burst_time[c2]
            waiting_time2 = waiting_time + burst_time[c2]
        print "P", process[c1], "      ", burst_time[c1], "          ", waiting_time, "          ", waiting_time2 - arrival_time[c1]
