# pythonMultiThreading

> pip install fastapi

> fastapi dev main.py

Server will get Started at the port 8000

Make a request to the local host on "task" end point with "inputVal" as the query

Example:

> http://127.0.0.1:8000/task/?inputVal=12


## Question 

Question : You are given a directed acyclic graph which stores the next and previous 
nodes, in which each node consists of a mathematic operation, you would need to 
generate a random number from 1 to 100 and perform that operation with the input value 
for that node. The input value for the current node will be the output value for the next node 
on the same level. For different level the input value will be the max value of output from 
the previous level. The levels are increased when 2 nodes are merged. The final answer will 
always be the last node where the nodes were merged.

![Screenshot from 2024-06-12 13-21-22](https://github.com/zeeCode15/pythonMultiThreading/assets/89879537/87bc7ecd-9311-480b-8452-8424cfba60f7)

Write this code in Python and then create an API of this code using any python framework 
which works best for parallelism. Also write an explanation regarding how you have verified 
the parallelism and also explain the max number of requests that you could execute in 
parallel. You can also write your own logic to achieve parallelism with the help of a python 
framework.


## Solution:

myModule.py

Here my lowest level starts with level 1.
The Graph is DAG (Directed Acyclic Graph)

Input value is same for all at Level 1 (The entry point)

Used Topological Sort to solved it:
1. Helped to increase the level by using the indegree to the Node, Child node will have indegree (Inside direct edges ) from the parent.(child level = sum of parents levels)
2. In the same manner maximum of the parents are inherited to the child Node.
3. A Random number is generated and The operation is performed with the random number between 1 to 100 with the operator stored in the node.

For Parallel Execusion:
1. From "concurrent.futures", "ThreadPoolExecutor" is imported to create the threads
2. With the help of "BackgroundTasks" from "fastapi", the threads are allocated to the background without breaking the flow of the code.


# Test with ApacheBench

Download the Zip from https://www.apachelounge.com/download/

Add the ab.exe to the path Variable (Windows)

run the command when your sever is up and running

> ab -n 100 -c 10 http://127.0.0.1:8000/task/?inputVal=15


