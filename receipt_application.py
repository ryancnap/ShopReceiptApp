"""
	receipt_application.py
	This is a small, procedurally-oriented (for now) application for Python 2.7x
	It's intended to serve as a recipt manager for a small, privately-owned
	automotive shop.
	I've kept it fairly general: the user (presumably the shop owner) has
	the option of choosing to add a customer record or view a new one.
	When viewing a customer record, we simply read from a previously-
	created text file. When adding a customer, we supply the name,
	vehicle year/make/model (maybe use this as a basis for search later?)
	date created/modified, how much said customer will be charged, and
	a short description of the job to be performed.
"""

# I'd very much like to refactor this into an object-oriented design, but I
# wanted to get the logic down first.
# Also a want for this is to maybe store customer info in JSON format for
# portability, and a barebones local sqlite db instead of unmanageable plethora
# of text files:)
# Hoping an OO refactor will help with the way I'm adding fields to
# *customer_info* in the *add_customer* function; too brittle as-is,
# whenever you choose to add an option to the prompt you then have to scroll
# down and remember to add the corresponding option to the *customer_info* dict.

import decimal
import time

def main():

	# Pretty print for current date in mm/dd/yyyy format.
	modification_date = time.strftime("%m/%d/%y")

	def add_customer(name = ""):

		# get customer info.
		name = raw_input("\nEnter customer's name: ")
		vehicle = raw_input("Enter the year, make, and model of the vehicle. Example: 2000 Ford Explorer\n> ")
		cost = decimal.Decimal(raw_input("How much will the customer be charged? ($00.00) $"))
		job = raw_input("Enter a short description of services being performed: ")

		#append to a list.
		customer_info = {
		"Date:": modification_date,
		"Name:": name,
		"Vehicle:": vehicle,
		"Cost of services:": cost,
		"Description of job:": job
		}

		customer_file = str(customer_info["Name:"]) + '.txt'
		customer_file = customer_file.replace(' ', '-')
		customer_file = customer_file.lower()
		print customer_file
		with open(customer_file, 'w') as out_file:
			for field in customer_info:
				print field, customer_info[field]
				out_file.write(str(field))
				# I do not approve of the following line; I simply ran out of coffee.
				out_file.write(' ' + str(customer_info[field]) + '\n')


	def view_customer():
		name = raw_input("\nEnter customer's name to view financial records: ")
		customer_file = str(name + '.txt').replace(' ', '-')
		customer_file = customer_file.lower()
		try:
			with open(customer_file, 'r') as in_file:
				for line in in_file:
					print line,
		except IOError:
			print "Error: Cannot find the file for {}".format(name)
			action()

	def action():
		""" This will loop displaying the choices dictionary until the user chooses a valid
			choice, ie add or view a customer, or exit the application. Need to implement add/view
			functions for the customers. This will allow adding a user and viewing a user's info.
		"""
		running = True
		while running == True:
			print "Please select a choice: "
			choices = dict(
				add = '***Add new customer***',
				view = '***View existing customer***',
				exit = '***Exit***',
				)

			for choice in choices:
				print choices[choice]

			# Prompt user for input, lower-case it to match dict keys.
			prompt = raw_input("\n> ").lower()
			error = "The choice {} could not be found.\n\n".format(prompt)

			# Try to get the user input from the dict, otherwise print error that was passed to function.
			print choices.get(prompt, error)

			# Check user input, run appropriate function(s).
			if prompt == 'add':
				print "***ADD EXISTING CUSTOMER***"
				add_customer()
				break
			elif prompt == 'view':
				print "***VIEW EXISTING CUSTOMER"
				view_customer()
				break

			elif prompt == "exit":
				print "***EXITING APPLICATION...***"
				# exit function goes here
				break

			else:
				continue


	action() # first function ran.

if __name__ == "__main__": main()