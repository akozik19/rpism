from matplotlib.pyplot import *
from numpy import *
from scipy.stats import norm

question_marks: list = [3, 8, 18, 23, 34, 43]


# Losowy rzut kością do gry
def roll_dice(custom_dice=None) -> int:
	if not custom_dice:
		return random.randint(1, 7)
	else:
		return random.choice(custom_dice)


# Funkcja symuluje 7 rzutów i wyznacza w którym rzucie udało się stanąć na pytajniku DOKŁADNIE 1 RAZ
def simulate_rolling(field: int, rolls_count: int) -> int:
	roll_no: int = 0
	result: bool = False

	for j in range(1, rolls_count):
		field += roll_dice()

		if result is False:
			roll_no += 1

		if field in question_marks:
			if result is True:
				return 0
			result = True

	if result is True:
		return roll_no
	return 0


# Funckja do zadania 4
def exercise_4(attempts: list, rolls_list: list, number_of_rolls: int) -> None:
	largest_j: int = 0
	roll_number: int = rolls_list[0]

	# Szukamy rzutu, który ma największe szanse na wykonanie się zdarzenia
	for j in rolls_list:
		j_occurrences: int = rolls_list.count(j)
		if j_occurrences > largest_j:
			largest_j = j_occurrences
			roll_number = j

	# Usuwamy wszystkie większe elementy tablicy większe od k
	for k in range(roll_number + 1, max(rolls_list) + 1):
		rolls_list = list(filter(lambda a: a != k, rolls_list))

	rolls_list.sort()
	# rysowanie wykresu dystrybuanty
	p: ndarray = norm.cdf(rolls_list, 1, 2)

	scatter(rolls_list, p, c='blue')
	for m in range(min(rolls_list)):
		scatter(m, 0, c='blue')

	for x, y in zip(rolls_list, p):
		label: str = "%.5f" % y
		annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

	title('Dystrybuanta')
	show()

	# rysowanie wykresu prawdopodobieństwa
	prob = []
	for n in attempts:
		prob.append(n / number_of_rolls)
	plot([0, 1, 2, 3, 4, 5, 6, 7], prob, 'ro')
	title('Prawdopodobienstwo')
	show()


def exercise_5(number_of_rolls: int) -> None:
	ranges: list = [1, 10, 50, 100]
	limit: list = []

	for j in ranges:
		list_range: list = []

		for i in range(j):
			probability, attempts, rolls_list = calculate_probability(0, 8, number_of_rolls)
			list_range += rolls_list
		limit.append(list_range)

	k: int = 0

	fig, ax = subplots(2, 2, figsize=(8, 8))
	for i in range(0, 2):
		for j in range(0, 2):
			ax[i, j].hist(limit[k], bins=[4, 5, 6, 7, 8], density=True)
			ax[i, j].set_title(label='Powtórzeń: ' + str(ranges[k]))
			k = k + 1
	show()


def calculate_probability(field: int, rolls_count: int, number_of_rolls: int) -> tuple:
	success_sum: int = 0
	attempts: list = [0, 0, 0, 0, 0, 0, 0, 0]
	rolls_list: list = []
	for x in range(1, number_of_rolls):
		roll_no: int = simulate_rolling(field, rolls_count)
		if roll_no:
			success_sum += 1
			attempts[roll_no] += 1
			rolls_list.append(roll_no)

	probability: float = success_sum / number_of_rolls
	return probability, attempts, rolls_list


def sum_of_rolls(rolls_number: int, attempts: int, custom_dice: list = None) -> list:
	result: list = []

	for x in range(attempts):
		roll_sum: int = 0
		for i in range(rolls_number):
			roll_sum += roll_dice(custom_dice)
		result.append(roll_sum)
	return result


def exercise_6(num_rolls_to_sum: int, attempts: int) -> None:
	custom_dice_1: list = [1, 2, 6, 7]
	custom_dice_2: list = [3, 4, 4, 8]

	roll_sum_dice_1: list = sum_of_rolls(num_rolls_to_sum, attempts, custom_dice_1)
	roll_sum_dice_2: list = sum_of_rolls(num_rolls_to_sum, attempts, custom_dice_2)

	average_1: int = sum(roll_sum_dice_1) / len(roll_sum_dice_1)
	average_2 = sum(roll_sum_dice_2) / len(roll_sum_dice_2)
	variance_1 = sum([(x - average_1) ** 2 for x in roll_sum_dice_1]) / len(roll_sum_dice_1)
	variance_2 = sum([(x - average_2) ** 2 for x in roll_sum_dice_2]) / len(roll_sum_dice_2)

	print("Kostka 1 [1, 2, 6, 7]:")
	print(f"Średnia: {average_1}")
	print(f"Wariancja: {variance_1}\n")
	print("Kostka 1 [3, 4, 4, 8]:")
	print(f"Średnia: {average_2}")
	print(f"Wariancja: {variance_2}\n")


if __name__ == '__main__':
	while True:
		try:
			number_of_attempts: int = int(input("Ilość prób:   "))
		except ValueError:
			print("Nieodpowiedni znak!")
			continue

		if number_of_attempts < 0:
			print("Nieodpowiednia wartość!")
			continue
		else:
			break

	while True:
		try:
			exercise_no = int(input("Podaj numer zadania:   "))
		except ValueError:
			print("Nieodpowiedni znak!")
			continue

		if exercise_no == 1:
			final_probability, counted_attempts, result_rolls_list = calculate_probability(0, 8, number_of_attempts)
			print(f"Prawdopodobienstwo wynosi {final_probability}")
			break
		elif exercise_no == 2:
			final_probability, counted_attempts, result_rolls_list = calculate_probability(3, 7, number_of_attempts)
			print(f"Prawdopodobienstwo wynosi {final_probability}")
			break
		elif exercise_no == 3:
			final_probability, counted_attempts, result_rolls_list = calculate_probability(0, 8, number_of_attempts)
			length = len(counted_attempts)
			for i in range(length - 1):
				print(f"Liczba pomyślnych prób w rzucie numer {i + 1} wynosi {counted_attempts[i + 1]}")
			break
		elif exercise_no == 4:
			final_probability, counted_attempts, result_rolls_list = calculate_probability(0, 8, number_of_attempts)
			exercise_4(counted_attempts, result_rolls_list, number_of_attempts)
			break
		elif exercise_no == 5:
			exercise_5(number_of_attempts)
			break
		elif exercise_no == 6:
			exercise_6(4, 50)
			break
		else:
			print("Nieprawidłowy numer zadania!")
			continue
