# Trafiasz na dokładnie jeden znak zapytania.
question_marks: list = [3, 8, 18, 23, 34, 43]


def task1() -> float:
	counter: int = 0
	for i in range(1, 8):
		for j in question_marks:
			if 6 * i >= j - 1 >= 1 * i:
				counter += 1
	return counter / 42


def task2() -> float:
	counter: int = 0
	for i in range(2, 8):
		for j in question_marks:
			if 6 * i >= j + 2 >= 1 * i:  # j - 1 + 3
				counter += 1
	return counter / 42


def task3() -> int:
	k: int = 0
	biggest_count: int = 0

	for i in range(1, 8):
		counter: int = 0
		for j in question_marks:
			if 6 * i >= j - 1 >= 1 * i:
				counter += 1
		if counter > biggest_count:
			biggest_count = counter
			k = i
	return k
