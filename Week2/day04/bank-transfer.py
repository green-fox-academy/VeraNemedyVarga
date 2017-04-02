accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an balance of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - balance
#
# Print "404 - account not found" if any of the account numbers don't exist

def name_balance(data_list):
    for client_data in data_list:
        namebalance = client_data["client_name"], client_data["balance"]
        print(namebalance)

name_balance(accounts)

def transfer(from_account_number, to_account_number, balance):
	for client_data in accounts:
		if from_account_number == client_data['account_number']:
			client_data['balance']=client_data['balance'] - balance
		if to_account_number == client_data['account_number']:
			client_data['balance'] = client_data['balance']+balance
	print(accounts)

transfer(11234543, 43546731, 0.2)

def validator(account_number):
	for client_data in accounts:
		if account_number == client_data['account_number']:
			return True


def double_validator(from_account_number, to_account_number):
	if validator(from_account_number) and validator(to_account_number):
		return
	else:
		print("404 - account not found")


double_validator(11234543, 43546731)
