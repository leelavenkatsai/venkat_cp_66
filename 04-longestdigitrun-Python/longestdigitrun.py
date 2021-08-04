# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	# pass
	n = abs(n)
	cnt_0 = 0
	cnt_0_temp = 0
	cnt_1 = 0
	cnt_1_temp = 0
	cnt_2 = 0
	cnt_2_temp = 0
	cnt_3 = 0
	cnt_3_temp = 0
	cnt_4 = 0
	cnt_4_temp = 0
	cnt_5 = 0
	cnt_5_temp = 0
	cnt_6 = 0
	cnt_6_temp = 0
	cnt_7 = 0
	cnt_7_temp = 0
	cnt_8 = 0
	cnt_8_temp = 0
	cnt_9 = 0
	cnt_9_temp = 0

	x=n
	max_cnt = 0
	max_val = 0
	while(x>0):
		d = x%10
		if(d==0):
			cnt_0_temp+=1
			if(cnt_0_temp>cnt_0):
				cnt_0=cnt_0_temp
				if(cnt_0>max_cnt):
					max_cnt = cnt_0
					max_val = 0
		else:            
			cnt_0_temp = 0

		if(d==1):
			cnt_1_temp+=1
			if(cnt_1_temp>cnt_1):
				cnt_1=cnt_1_temp
				if(cnt_1>max_cnt):
					max_cnt = cnt_1
					max_val = 1
		else:
			cnt_1_temp = 0

		if(d==2):
			cnt_2_temp+=1
			if(cnt_2_temp>cnt_2):
				cnt_2=cnt_2_temp
				if(cnt_2>max_cnt):
					max_cnt = cnt_2
					max_val = 2
		else:
			cnt_2_temp = 0

		if(d==3):
			cnt_3_temp+=1
			if(cnt_3_temp>cnt_3):
				cnt_3=cnt_3_temp
				if(cnt_3>max_cnt):
					max_cnt = cnt_3
					max_val = 3
		else:
			cnt_3_temp = 0

		if(d==4):
			cnt_4_temp+=1
			if(cnt_4_temp>cnt_4):
				cnt_4=cnt_4_temp
				if(cnt_4>max_cnt):
					max_cnt = cnt_4
					max_val = 4
		else:
			cnt_4_temp = 0

		if(d==5):
			cnt_5_temp+=1
			if(cnt_5_temp>cnt_5):
				cnt_5=cnt_5_temp
				if(cnt_5>max_cnt):
					max_cnt = cnt_5
					max_val = 5
		else:
			cnt_5_temp = 0

		if(d==6):
			cnt_6_temp+=1
			if(cnt_6_temp>cnt_6):
				cnt_6=cnt_6_temp
				if(cnt_6>max_cnt):
					max_cnt = cnt_6
					max_val = 6
		else:
			cnt_6_temp = 0

		if(d==7):
			cnt_7_temp+=1
			if(cnt_7_temp>cnt_7):
				cnt_7=cnt_7_temp
				if(cnt_7>max_cnt):
					max_cnt = cnt_7
					max_val = 7
		else:
			cnt_7_temp = 0

		if(d==8):
			cnt_8_temp+=1
			if(cnt_8_temp>cnt_8):
				cnt_8=cnt_8_temp
				if(cnt_8>max_cnt):
					max_cnt = cnt_8
					max_val = 8
		else:
			cnt_8_temp = 0

		if(d==9):
			cnt_9_temp+=1
			if(cnt_9_temp>cnt_9):
				cnt_9=cnt_9_temp
				if(cnt_9>max_cnt):
					max_cnt = cnt_9
					max_val = 9
		else:
			cnt_9_temp = 0
		x//=10

	if(max_cnt==cnt_0):
		return 0
	elif(max_cnt==cnt_1):
		return 1
	elif(max_cnt==cnt_2):
		return 2
	elif(max_cnt==cnt_3):
		return 3
	elif(max_cnt==cnt_4):
		return 4
	elif(max_cnt==cnt_5):
		return 5
	elif(max_cnt==cnt_6):
		return 6
	elif(max_cnt==cnt_7):
		return 7
	elif(max_cnt==cnt_8):
		return 8
	elif(max_cnt==cnt_9):
		return 9