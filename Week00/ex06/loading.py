from time import sleep, time
from sys import stdout
from tqdm import tqdm

#ETA: 8.67s [ 23%][=====>                    ] 233/1000 | elapsed time 2.33s

progressBarLen = 26

def progress_visualizer(iteration, elapsedTime, iterationsNumber):
	progress = iteration / iterationsNumber * 100
	if progress == 0:
		return
	progressChars = progress / 100 * progressBarLen
	ETA = (elapsedTime / progress * 100) - elapsedTime
	bar = ('=' * int(progressChars - 1) + '>').ljust((progressBarLen), ' ')
	print(f"ETA: {ETA:.2f}s [ {int(progress)}%][{bar}]",end='')
	print(f"{iteration}/{iterationsNumber} | elapsed time {elapsedTime:.2f}s", end='\r')

def ft_progress(lst):
	iteration = 1
	t0 = time()
	elapsedTime = 0
	iterationsNumber = len(lst)
	for elm in lst:
		elapsedTime = time() - t0
		callTime = time()
		yield elm
		progress_visualizer(iteration, elapsedTime, iterationsNumber)
		iteration += 1
	print()


tab = range(1000)

number = 0
for elm in ft_progress(tab):
	number += elm
	sleep(0.01)
print(number)