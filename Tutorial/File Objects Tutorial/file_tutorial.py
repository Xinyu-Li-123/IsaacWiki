
def dumbWay():
    f = open('test.txt', 'r')

    print(f.name)
    print(f.mode)

    f.close()

def smartWay():
    # the smart way: use a context manager to open a file
    # create a block to handle file,
    #   close it automatically when exiting the block or an exception occurs
    with open('test.txt', 'r') as f:
        # .read() returns the content as a string,
        # .readline() returns one line as a string
        # .readlines() returns all lines as a list

        for line in f:
            # avoid storing tons of lines in the memory
            print(line, end='')


    # Even if we exit with block,
    #       we still have access to the file
    print(f.name)
    # But we can't read from a closed file.
    try:
        print(f.read())
    except ValueError as err:
        print(f"ValueError: {err}")

def smartWay2():
    # to read a large file, we'd like to read one chunk at a time
    with open('test.txt', 'r') as f:
        size_to_read = 10

        f_contents = f.read(size_to_read)
        print(f_contents, end='')
        print(f.tell()) # location of file pointer

        f.seek(0)       # move file pointer to position 0
        f_contents = f.read(size_to_read)
        print(f_contents, end='')

        # while len(f_contents) > 0:
        #     print(f_contents, end='*')
        #     f_contents = f.read(size_to_read)

def writeAndCopyFile():
    with open('test.txt', 'r') as rf:
        with open('test_copy.txt', 'w') as wf:
            for line in rf:
                wf.write(line)

def copyPicFile():
    with open('Abigail.jpg', 'rb') as rf:
        with open('Abigail_copy.jpg', 'wb') as wf:
            # read ana write using binary mode
            # for line in rf:
            #     wf.write(line)
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            # for i in range(300):
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)

# dumbWay()
# smartWay()
# smartWay2()
# writeAndCopyFile()
# copyPicFile()