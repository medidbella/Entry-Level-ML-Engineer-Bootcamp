from time import sleep, time
from sys import stdout, exit
from tqdm import tqdm


progressBarLen = 26

def progress_visualizer(iteration, elapsedTime, iterationsNumber):
	progress = iteration / iterationsNumber * 100
	if progress == 0:
		return
	progressChars = progress / 100 * progressBarLen
	ETA = (elapsedTime / progress * 100) - elapsedTime
	bar = ('=' * int(progressChars - 1) + ('>' if progress < 100 else '=')).ljust((progressBarLen), ' ')
	print(f"ETA: {ETA:.2f}s [{int(progress):3}%][{bar}]",end='')
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

tab = range(1000)

number = 0
for elm in ft_progress(tab):
	number += elm
	sleep(0.01)
print()
print(number)