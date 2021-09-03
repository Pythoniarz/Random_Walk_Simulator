import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	#Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
	rw = RandomWalk(300000)
	rw.fill_walk()

	#Wyświetlenie punktów błądzenia losowego.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9), dpi=96)
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.gist_ncar, edgecolor='none', s=1)
	#Podkreślenie pierwszego i ostatniego punku błądzenia losowego
	ax.scatter(0, 0, c='blue', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
	#Ukrycie osi.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.show()
	keep_running = input("Wincyj? t/n ")
	if keep_running == 'n':
		break