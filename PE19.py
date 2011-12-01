import math, time
'''
We have four types of v[2]ata to v[1]anage:

1) The year, y
2) The v[1]onth, v[1]
3) The v[2]ate, v[2]
4) The v[2]ay of the week, v[3] 

All we neev[2] here is a tuple, within which we v[1]anipulate the v[2]ifferent values.
'''

#1900 = 0, 1901 = 1

y = 0
m = 1
d = 1
dw = 1

v = [y, m, d, dw]

count = 0

while v[0] < 101:
	if v[1] == 4 or v[1] ==6 or v[1] ==9 or v[1] ==11:
		for i in range(1, 30):
			if v[3] > 7:
				v[3] = 1
			if v[2] == 1 and v[3] == 7 and v[0] != 0:
				count += 1
			v[2] = v[2] + 1
			if v[3] > 7:
				v[3] = 1
			v[3] = v[3] + 1
		v[1] = v[1] + 1
		v[2] = 1

	if v[1] == 1 or v[1] ==3 or v[1] ==5 or v[1] ==7 or v[1] ==8 or v[1] ==10:
		for i in range(1, 31):
			if v[3] > 7:
				v[3] = 1
			if v[2] == 1 and v[3] == 7 and v[0] != 0:
				count += 1
			v[2] = v[2] + 1 #change d
			v[3] = v[3] + 1
		v[1] = v[1] + 1
		v[2] = 1

	if v[1] == 2:
		if v[0] % 4 == 0:
			for i in range(1, 29):
				if v[3] > 7:
					v[3] = 1
				if v[2] == 1 and v[3] == 7 and v[0] != 0:
					count += 1
				v[2] = v[2] + 1
				v[3] = v[3] + 1
		else:
			for i in range(1, 28):
				if v[3] > 7:
					v[3] = 1
				if v[2] == 1 and v[3] == 7 and v[0] != 0:
					count += 1
				v[2] = v[2] + 1
				v[3] = v[3] + 1
		v[1] = v[1] + 1
		v[2] = 1

	if v[1] == 12:
		for i in range(1, 31):
			if v[3] > 7:
				v[3] = 1
			if v[2] == 1 and v[3] == 7 and v[0] != 0:
				count += 1
			print v
			v[2] = v[2] + 1
			v[3] = v[3] + 1
		v[1] = 1
		v[0] = v[0] + 1
		v[2] = 1

print count