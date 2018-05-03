# first come first serve
n = input("enter number of processes:")
print n

burst_time = [0]*n
arrival_time = [0]*n
process=[0]*n

for c1 in range(n):
    burst_time[c1] = input("enter burst time:")

    arrival_time[c1] = input("enter arrival time:")
    process[c1]=input("enter process number:")
for c1 in range(n):
    print "burst time of processes:"
    print burst_time[c1]

for c1 in range(n):
    for c2 in range(n-1):

        if arrival_time[c2] > arrival_time[c2+1]:

            temp = arrival_time[c2]
            arrival_time[c2] = arrival_time[c2+1]
            arrival_time[c2+1] = temp

            temp1 = burst_time[c2]
            burst_time[c2] = burst_time[c2+1]
            burst_time[c2+1] = temp1

            temp2 = process[c2]
            process[c2] = process[c2 + 1]
            process[c2 + 1] = temp2

print "Process burst time waiting time turnaround time"
turnaround_time = [0]*n
waiting_time = [0]*n
waiting_time2 = [0]*n
for c1 in range(n):

    if c1 == 0:
        turnaround_time[c1] = burst_time[c1]
        print "P", process[c1], "     ", burst_time[c1], "      ", waiting_time[c1], "      ", turnaround_time[c1]
    elif c1 > 0:
        for c2 in range(c1):
            waiting_time[c1] += burst_time[c2]
            waiting_time2[c1] = waiting_time[c1] + burst_time[c2]
            turnaround_time[c1] = waiting_time2[c1] - arrival_time[c1]
        print "P", process[c1], "     ", burst_time[c1], "      ", waiting_time[c1], "     ", turnaround_time[c1]

average = 0.0
total = 0
for c1 in range(n):
    total += turnaround_time[c1]
average = (total/n)*100
print "average turnaround time:", average

total_waiting = 0
for c1 in range(n):
    total_waiting += waiting_time[c1]
print "total waiting time:", total_waiting
