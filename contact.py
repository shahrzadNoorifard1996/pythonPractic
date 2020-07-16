import sys
import csv

DB_FILE_NAME = 'db.csv';


def list_all():
	with open(DB_FILE_NAME) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0;
	    for row in csv_reader:
	        print(", ".join(row))
	        line_count+=1

	    print(f'Processed {line_count} lines.\n')

	main()


def add_new():
	with open(DB_FILE_NAME, mode='a') as csv_file:
	    fieldnames = ['name', 'number']
	    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	    name = input('Enter the name: ')
	    number = input('Enter the number: ')
	    writer.writerow({'name': name, 'number': number})

	main()

# name,number
# Brad,239842934
# Ashley,2938432

def remove_contact():
    lines = list()
    name = input("Please enter a name to be deleted: ")
    with open(DB_FILE_NAME, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == name:
                    lines.remove(row)

    with open(DB_FILE_NAME, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    print('done\n')
    main()


def search_by_name():
    name = input("Please enter a name to search for: ")
    with open(DB_FILE_NAME, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if row[0] == name:
                print(f'{row[0]}: {row[1]}\n')

    main()


def search_by_number():
	number = input("Please enter a number to search for: ")
	with open(DB_FILE_NAME, 'r') as readFile:
		reader = csv.reader(readFile)
		for row in reader:
			if row[1] == number:
				print(f'{row[0]}: {row[1]}\n')

	main()


def print_help():
	print('Choose between following options: ')
	print('1\tlist all contacts')
	print('2\tadd new contact')
	print('3\tremove a contact by name')
	print('4\tfind a contact by name')
	print('5\tfind a contact by number\n')
	print('help\tprint help')
	print('exit\texit program\n')
	main()


def main():
	# get command from user
	command = input('_> ');

	# check the command and execute if correct
	if command == '1':
		list_all()
	elif command == '2':
		add_new();
	elif command == '3':
		remove_contact();
	elif command == '4':
		search_by_name()
	elif command == '5':
		search_by_number()
	elif command == 'help':
		print_help()
	elif command == 'exit':
		sys.exit()
	else:
		print('Unknown command. Please try again or type exit to finish\n')
		main()




if __name__ == '__main__':
	print_help();
	main()