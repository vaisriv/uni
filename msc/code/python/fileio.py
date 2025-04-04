nums = [2, 3, 4, 5, 6]
nums = map(str, nums)
f = open("demofile3.txt", "a")
nums_out = [num + str("\n") for num in nums]
f.writelines(nums_out)
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
