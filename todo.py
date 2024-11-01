import os

TODO_FILE = 'todo.txt'

def load_tasks():
	if os.path.exists(TODO_FILE):
		with open(TODO_FILE,'r') as file:
			return file.read().splitlines()
	return []

def save_tasks(tasks):
	with open(TODO_FILE,'w') as file:
		file.write('\n'.join(tasks))

def add_task(task):
	tasks = load_tasks()
	tasks.append(task)
	save_tasks(tasks)
	print(f'Added task: {task}')

def view_tasks():
	tasks = load_tasks()
	if tasks:
		print("To-Do List:")
		for index, task in enumerate(tasks,start=1):
			print(f'{index}.{task}')
	else:
		print("No tasks in the To-Do List")

def remove_task(index):
	tasks = load_tasks()

	if 0 < index <= len(tasks):
		removed = tasks.pop(index - 1)
		save_tasks(tasks)
		print(f'Removed task: {removed}')
	else:
		print('Invalid task number')

def main():
	while True:
		print('/n TO-Do List Application')
		print('1. Add task')
		print('2. View tasks')
		print('3. Remove task')
		print('4. Exit')

		choice = input('Choose as option:')

		if choice == '1':
			task = input('Enter the task:')
			add_task(task)
		elif choice =='2':
			view_tasks()
		elif choice =='3':
			try:
				index = int(input('Enter task number to remove:'))
				remove_task(index)
			except ValueError:
				print('Pless enter a valid number')
		elif choice =='4':
				break
		else:
			print('Invalid choice, plese try again')

if __name__ == '__main__':
	main()
