#bt=burst time
#wt=waiting time
#tat=turn around time
#This code gives the round robbin algorithm parameters as output such as mentioned above
def findWaitingTime(processes, task, bt,  wt, quantum):  #function to find the waiting time
    rem_bt = [0] * task
    for i in range(task):  				#quantum=time-slice or maximum time given to one process at a time
        rem_bt[i] = bt[i] 
    t = 0  
    while(True): 
        done = True
        for i in range(task): 
            if (rem_bt[i] > 0) : 
                done = False 
                if (rem_bt[i] > quantum) : 
                    t = t+ quantum  
                    rem_bt[i] -= quantum  
                else: 
                    t = t + rem_bt[i]  
                    wt[i] = t - bt[i]                    
                    rem_bt[i] = 0                  
        if (done == True): 
            break
                
def findTurnAroundTime(processes, task, bt, wt, tat):     #turn-around-time=burst-time+waiting time i.e. total time residing in the process
    for i in range(task): 
        tat[i] = bt[i] + wt[i] 
    
def findavgTime(processes, task, bt, quantum):
    wt = [0] * task
    tat = [0] * task
    findWaitingTime(processes, task, bt,wt, quantum)  
    findTurnAroundTime(processes, task, bt, wt, tat)  
    print("Processes\tBurst Time\tWaiting Time\tTurn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(task):
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", i + 1, "\t\t", bt[i],  "\t\t", wt[i], "\t\t", tat[i])
    print("\nAverage waiting time = %.5f "%(total_wt /task) ) #average waiting time of all the processes
    print("Average turn around time = %.5f "% (total_tat / task)) #average turn-around-time of all the processes

			
					
if __name__ =="__main__": #starting main function or driver program to run the entire code

	task=int(input("Please Enter the number of task: "))
	jobs=[]

	for i in range(task):                                            #take execution time more than the quantum to clear about round-robin
		jobs.append(list(map(int,input("Enter Source,Destination,Tool Conflict,ExecutionTime\n").strip().split(",")))) 

	burst_time=[]
	proc=[]
	quantum=20
	for i in range(task):
		burst_time.append(int(jobs[i][3]))
		proc.append(i+1)
	findavgTime(proc, task, burst_time, quantum) 
