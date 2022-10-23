def read_large_file(file_object, keywords):
    for line in file_object:
        return_line = False
        for keyword in keywords:
            if keyword.lower() in set(line.lower().split()):
                return_line = True
        if return_line:
            yield line