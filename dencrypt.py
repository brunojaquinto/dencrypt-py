from cryptography.fernet import Fernet

with open('key.key', 'rb') as key_file:
	key = key_file.read()

f = Fernet(key)

print('\n== FILE ENCRYPTION TOOL ==\n== SECURE YOUR FILES EASILY ==\n\n')
user_action = input('1- Encrypt\n2- Decrypt\n\nSelect operation: ')

if user_action == '1':
	file_name = input('File to encrypt: ')

	with open(file_name, 'rb') as file:
		data = file.read()

	encrypted_data = f.encrypt(data)

	with open(file_name +  '_e', 'wb') as file:
		file.write(encrypted_data)

	print(f'\nEncryption completed. Output: {file_name}_e')

elif user_action == '2':
	file_name = input('File to decrypt: ')

	with open(file_name, 'rb') as file:
		encrypted_data = file.read()

	decrypted_data = f.decrypt(encrypted_data)

	with open(file_name + '_d', 'wb') as file:
		file.write(decrypted_data)

	print(f'Decryption completed. Output: {file_name}_d')
else:
	print('Error: Invalid option.')
