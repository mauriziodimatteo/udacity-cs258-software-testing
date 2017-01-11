# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list.
# The return value of the fuzzit procedure should be a list of
# byte-modified strings.


import math
import random

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


def fuzzit(content):
    # Write a random fuzzer for a simulated text viewer application

    FuzzFactor = 5
    num_iter = 100

    fuzzed_data = []

    for _ in range(num_iter):

        buf = bytearray(content, 'ascii')
        numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1

        for _ in range(numwrites):
            # Create a random byte.
            rand_byte = random.randrange(256)
            # Pick a random location in the buffer.
            rand_n = random.randrange(len(buf))
            # Replace the byte.
            buf[rand_n] = "%c" % rand_byte

        fuzzed_data.append(str(buf))

    return fuzzed_data


# Uncomment to run locally.
# print fuzzit(content)
