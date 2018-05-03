n = input("enter number of processes: ")
burst_time = [0]*n
arrival_time = [0]*n
r_burst_time = [0]*n
process = [0]*n
waiting_time = [0]*n
turnaround_time = [0]*n

total_waiting = 0
total_turnaround = 0

quantum = input("enter quantum time: ")

for c1 in range(n):
    burst_time[c1] = input("enter burst time: ")
    arrival_time[c1] = input("enter arrival time:")
    process[c1] = input("enter process name:")
# creating copy of burst times

for c1 in range(n):
    r_burst_time[c1] = burst_time[c1]
# sorting arrays

for c1 in range(n-1):
    if arrival_time[c1] > arrival_time[c1+1]:
        temp = arrival_time[c1]
        arrival_time[c1] = arrival_time[c1+1]
        arrival_time[c1+1] = temp

        temp = burst_time[c1]
        burst_time[c1] = burst_time[c1 + 1]
        burst_time[c1 + 1] = temp

        temp = process[c1]
        process[c1] = process[c1 + 1]
        process[c1 + 1] = temp

current_time = 0

flag = 0
while flag == 0:

    for c1 in range(n):
        if r_burst_time[c1] > 0:

            if r_burst_time[c1] > quantum:
                current_time += quantum
                r_burst_time[c1] -= quantum
            elif r_burst_time[c1] <= quantum:
                current_time += r_burst_time[c1]
                waiting_time[c1] = current_time - burst_time[c1]
                r_burst_time[c1] = 0
        elif r_burst_time[c1] == 0:
            flag = 1

for c1 in range(n):
    turnaround_time[c1] = waiting_time[c1]+burst_time[c1]

for c1 in range(n):
    total_waiting += waiting_time[c1]
    total_turnaround += turnaround_time[c1]
print "process burst time waiting time turnaround time quantum"
for c1 in range(n):
    print "Process", process[c1], "    ", burst_time[c1], "     ", waiting_time[c1], "         ", turnaround_time[c1],"        ", quantum
print "total waiting time:", total_waiting
print "total turnaround time:", total_turnaround

average = total_turnaround/n
print "average turnaround time :", average
