# To Run this program,
# Press Command + Enter 





































import random
import time

print ("Welcome to the Multiplication Game")
print ("Two Numbers are randomly picked between 0 and 12")
print ("Try to Answer ASAP. If you do not answer in 3 seconds, You FAIL!")

score = 0

ready = input("\n\nAre you ready? (y/n): ")

while (ready == 'y'):

	first = random.randint(0,12)
	second = random.randint(0,12)


	for x in range(3,0,-1):
		print(x)
		time.sleep(1)

	print("\nQuestion: ")
	time1 = time.time()
	question = int(input(str(first) + " x " + str(second) + " = "))
	time2 = time.time()

	if (question == first * second and time2 - time1 < 3):
		print ("You got it!")
		score += 1
	else:
		if (time2 - time1 >= 3):
			print ("You did not get it in time.")
		else:
			print ("Wrong Answer.")

	print ("Score: " + str(score))
	ready = input("\n\nAre you ready? (y/n): ")

else:
	print ("Alright. Prepare yourself")
	print ("Total Score: " + str(score))