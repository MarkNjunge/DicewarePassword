import pickle
import os.path as path
import secrets
import sys


def get_dict():
    if path.exists('passes.pickle'):
        return pickle.load(open("passes.pickle", "rb"))
    else:
        passes = {}
        with open("diceware.wordlist.asc", "r") as f:
            lines = f.readlines()
            for line in lines:
                key = line.split("	")[0]
                value = line.split("	")[1]
                passes[key] = value
        pickle.dump(passes, open("passes.pickle", "wb"))
        print("Created pickle")
        return passes


def get_random_key():
    x = ""
    for i in range(0, 5):
        x += str(secrets.choice(range(1, 6)))
    return x


def main(pass_len):
	passes = get_dict()
	final = ""
	for i in range(0, pass_len):
	    key = get_random_key()
	    final += passes[key]
	print(final.replace("\n", " "))


if __name__ == '__main__':
	pass_len = 5
	pass_count = 1

	if len(sys.argv) > 1:
		pass_len = int(sys.argv[1])

	if len(sys.argv) > 2:
		pass_count = int(sys.argv[2])

	for i in range(0, pass_count):
		main(pass_len)

	
