# MapReduce---Hadoop---To-find-the-number-of-spikes-for-each-website-in-the-given-weblog
To find the number of spikes for each website in the given weblog
Problem to solve: You are given a weblog stored in a tab-separated 3-column file. 
Each line represents a website, start_datetime & end_datetime, e.g., “199.72.81.55 1995-08-20 05:08:01 1995-08-20 05:11:08” represents a website, user interaction start time, and user interaction end time. 
Your job is to find the number of spikes per website based on the user interaction time.
Spike: If the average time spent on a website per day has at least doubled two times continuously over three consecutive days then it is called a spike.

MapReduce Job 1: Finds the average number of seconds users spent on each website, for each day.

MapReduce Job 2: Identifies the spikes in this data.

MapReduce Job 3: Aggregates the counts to get number of spikes per website
