#www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum

import sys
commands = []
for line in sys.stdin:
	commands.append(line)
	
def sub(list):
	for line in list:
		if len(line) == 0:
			print(line, "False")
		nums = line.split()
		for n in nums:
			curr = int(n)
			if curr == 0:
				print(line, "True")
				return
			for x in nums:
				sum = curr + int(x)
				if sum == 0:
					print(line, "True")
					return
		print(nums, "False")
		return

sub(commands)