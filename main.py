import pickle
import os.path as path
import secrets
import sys
import urllib.request


def get_dict():
    # Return a pickle it exists, if not, download the wordlist and generate a pickle
    if path.exists('passes.pickle'):
        return pickle.load(open("passes.pickle", "rb"))
    else:
        print("Downloading wordlist...")
        passes = {}
        url = 'http://world.std.com/~reinhold/diceware.wordlist.asc'
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')

        # Remove PGP information
        lines = text.split("-----BEGIN PGP SIGNED MESSAGE-----")[1].split("-----BEGIN PGP SIGNATURE-----")[0].split("\n")

        for line in lines:
            if len(line) == 0:
                continue;

            key = line.split("\t")[0]
            value = line.split("\t")[1]
            passes[key] = value

        pickle.dump(passes, open("passes.pickle", "wb"))
        print("Created pickle")
        return passes


def get_random_key():
    x = ""
    # Create a random 5 character number to be used as an index
    for i in range(0, 5):
        x += str(secrets.choice(range(1, 6)))
    return x


def generate_pass(pass_len):
    passes = get_dict()
    final = ""
    for i in range(0, pass_len):
        key = get_random_key()
        final += passes[key]
        final += " "
    return final


if __name__ == '__main__':
    pass_len = 5
    pass_count = 1

    if len(sys.argv) > 1:
        pass_len = int(sys.argv[1])

    if len(sys.argv) > 2:
        pass_count = int(sys.argv[2])

    for i in range(0, pass_count):
        p = generate_pass(pass_len)
        print(p)
