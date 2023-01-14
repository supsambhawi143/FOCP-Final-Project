#TASK2final
#Program to display the best time here runner
import time

print("Park Run Timer")
print("~~~~~~~~~~~~~~")

print("Let's go!")


 # initializing the variables
tot_runners = 0
tot_time = 0
fastest_time = 0
slowest_time = 0
best_time = 0
best_time_here_runner = 0

 # prompts the user to enter data
while True:
    user_data = input("> ")
    if user_data == "END":
        break

    try:
    # get runner number and time
       runner_num, time = user_data.split("::")
    
    #converts runner number to int
       runner_num = int(runner_num)

    # converts time to int
       time = int(time)

    except ValueError:
        print("Error in data stream. Ignorning. Carry on.")
        continue
    
    # Adds total runners
    tot_runners += 1

    #Adds total time     
    tot_time += time
           
    if fastest_time == 0 or time < fastest_time:
            fastest_time = time
            best_time_here_runner = runner_num
            
    if slowest_time == 0 or time > slowest_time:
            slowest_time = time

if tot_runners == 0:
    print("No data found. Nothing to do. What a pity.")
else:
   # calculate average time
    avg_time = tot_time // tot_runners

# convert average time to minutes and seconds
    avg_time_min = int(avg_time / 60)
    avg_time_sec = int(avg_time % 60)

# convert fastest time to minutes and seconds
    fastest_time_min = int(fastest_time / 60)
    fastest_time_sec = int(fastest_time % 60)

# converts slowest time to minutes and seconds
    slowest_time_min = int(slowest_time / 60)
    slowest_time_sec = int(slowest_time % 60)

# prints the results
    print(f"Total Runners: {tot_runners}")
    print(f"Average Time:  {avg_time_min} minutes, {avg_time_sec} seconds")
    print(f"Fastest Time:  {fastest_time_min} minutes, {fastest_time_sec} seconds")
    print(f"Slowest Time:  {slowest_time_min} minutes, {slowest_time_sec} seconds")

    print(f"Best Time Here: Runner #{best_time_here_runner}")
