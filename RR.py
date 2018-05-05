No_Process=input("Enter No Of Processes \n")
print(No_Process)
n=int(No_Process)

Arrival_Time=[0]*n
Burst_Time=[0]*n
Turn_Around=[0]*n
Completion_Time=[0]*n
Remaining_burst=[0]*n
Waiting_Time=[0]*n
Total_Waiting_Time=0
Total_TurnAround=0
slice=input("Enter Quantam Time\n")
#Priority_No=[0]*n
for i in range(0,n):
	Arrival_Time[i]=input("Enter Arrival Time")
	Burst_Time[i]=input("Burst Time")
	#Priority_No[i]=input("Priority No")
for i in range(0,n):
    Remaining_burst[i] = Burst_Time[i]
for i in range (0,n-1):
	for j in range (0,n-1-i):
		if Arrival_Time[j]>Arrival_Time[j+1]:
			Arrival_Time[j],Arrival_Time[j+1]=Arrival_Time[j+1],Arrival_Time[j]
			Burst_Time[j],Burst_Time[j+1]=Burst_Time[j+1],Burst_Time[j]
TimeofState=0
for i in range(0, n):
    if Remaining_burst[i] > 0:
        if Remaining_burst[i] > slice:
            TimeofState += slice
            Remaining_burst[i] -= slice
        elif Remaining_burst[i] <= slice:
            TimeofState += Remaining_burst[i]
            Waiting_Time[i] = TimeofState - Burst_Time[i]
            Remaining_burst[i] = 0

print("Process  ","Arrival Time,Burst Time","Turn Around Item","Waiting Time")
for i in range(0,n):
	Turn_Around[i] =Waiting_Time[i]+Burst_Time[i]
for i in range(0,n):
    Total_TurnAround+=Turn_Around[i]
    Total_Waiting_Time+=Waiting_Time[i]
    print(i,Arrival_Time[i],Burst_Time[i],Turn_Around[i],Waiting_Time[i])
print("Total Waiting Time = ",Total_Waiting_Time)
print("Total TurnAroun Time = ",Total_TurnAround)
print("Average = ",Total_TurnAround/n)

