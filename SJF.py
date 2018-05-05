No_Process=input("Enter No Of Processes \n")
print(No_Process)
n=int(No_Process)

Arrival_Time=[0]*n
Burst_Time=[0]*n
Turn_Around=[0]*n
Waiting_Time=[0]*n
#Priority_No=[0]*n
for i in range(0,n):
	Arrival_Time[i]=input("Enter Arrival Time")
	Burst_Time[i]=input("Burst Time")
	#Priority_No[i]=input("Priority No")
least=Burst_Time[0]
print("Arrival Time")
for i in range (0,n-1):
	for j in range (0,n-1-i):
		if Burst_Time[j]>Burst_Time[j+1]:
			Burst_Time[j], Burst_Time[j + 1] = Burst_Time[j + 1], Burst_Time[j]
			Arrival_Time[j],Arrival_Time[j+1]=Arrival_Time[j+1],Arrival_Time[j]

print("Burst Time","Arrival Time ","Turn Around Item","Waiting Time")
for i in range(0,n):
	Turn_Around[i] =Arrival_Time[i]+Burst_Time[i]
	Waiting_Time[i]=Turn_Around[i]-Arrival_Time[i]
	print(Burst_Time[i],Arrival_Time[i],Turn_Around[i],Waiting_Time[i])
 