# Access Pi address_dict
import os
import ast

# FILE PATH
package_dir = os.path.dirname(os.path.abspath(__file__))
local_file = os.path.join(package_dir,'PiAddress.txt')

# Read file text
try:
    with open(local_file, 'rt') as file_text:
        file_text = file_text.read() # Read the text file
    address_dict = ast.literal_eval(file_text)
    print(address_dict)
except IOError:
    print("IOError: file PiAddress.txt not present in directory")
except NameError:
    print("NameError: file PiAddress.txt not present in directory")
except IndexError:
    print("IndexError: incomplete info in file")
except TypeError:
    print("TypeError: dictionary keys not indexable")
