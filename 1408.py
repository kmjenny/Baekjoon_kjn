# 24
import sys
now_time = list(map(int,sys.stdin.readline().split(':')))
start_time = list(map(int,sys.stdin.readline().split(':')))

total = (start_time[0]*3600+start_time[1]*60+start_time[2])-(now_time[0]*3600+now_time[1]*60+now_time[2])

if total<0:
    total += 60*60*24

x = total//3600
y = (total%3600)//60
z = total%60

print("%02d:%02d:%02d"%(x,y,z))