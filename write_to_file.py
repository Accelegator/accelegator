""" Write the specified information to the specified file """


def write(data, file_name):

    stored_file = open(file_name, 'a')
    stored_file.write("%s\n" % (data))
    stored_file.close
