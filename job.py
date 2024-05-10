def job_sequencing(jobs):
    
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    result = [None] * max_deadline
    total_profit = 0
    
    
    for job in jobs:
        deadline = job[1]
        for i in range(deadline - 1, -1, -1):
            if result[i] is None:
                result[i] = job[0]
                total_profit += job[2]
                break
                
    return result, total_profit

def take_job_input():
    jobs = []
    n = int(input("Enter the number of jobs: "))
    for i in range(n):
        job_id = input(f"Enter job ID for job {i+1}: ")
        deadline = int(input(f"Enter deadline for job {i+1}: "))
        profit = int(input(f"Enter profit for job {i+1}: "))
        jobs.append((job_id, deadline, profit))
    return jobs

# Examp
jobs = take_job_input()
sequence, profit = job_sequencing(jobs)
print("Job Sequence:", sequence)
print("Total Profit:", profit)
