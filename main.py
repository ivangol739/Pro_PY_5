import time
import os

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]

path = os.path.join(os.getcwd())

def logger_path(_path):
	def logger(function):
		def _logger(*args, **kwargs):
			function_name = function.__name__
			function_data = time.ctime()
			function_args = args
			function_kwargs = kwargs
			function_results = function(*args, **kwargs)
			data = f'Имя функции: {function_name} \n'  \
				   f'Время лога фукнции: {function_data} \n' \
				   f'Аргументы функции: {function_args} {function_kwargs} \n' \
				   f'Возвращаемое значение: {function_results} \n' \

			with open(f'{_path}\\logging.txt', 'a') as f:
				f.write(data)
			return function_results
		return _logger
	return logger

class FlatIterator:

	def __init__(self, list):
		self.list = [a for b in list for a in b]

	def __iter__(self):
		self.cursor = -1
		return self

	@logger_path(path)
	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.list):
			raise StopIteration
		return self.list[self.cursor]

for item in FlatIterator(nested_list):
	print(item)

@logger_path(path)
def flat_generator(a: list):
	yield [x for sublist in a for x in sublist]

for item in flat_generator(nested_list):
	print(item)
