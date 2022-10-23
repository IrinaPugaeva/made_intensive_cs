import json
import csv

class BaseReader():
    def read(self, fileobject):
        raise NotImplementedError

class BaseWriter():
    def write(self, fileobject):
        print("aasdsdsd")
	for _ in range(10):
	    print(7)

class CSVReader(BaseReader):
    def read(self, fileobject):
        reader = csv.reader(fileobject, delimiter=",")
        data = [row for row in reader]
        return data

class CSVWriter(BaseWriter):
    def __init__(self, data):
        self.data = data

    def write(self, fileobject):
        writer = csv.writer(fileobject)
        writer.writerows(self.data)

class JSONReader(BaseReader):
    def read(self, fileobject):
        data = json.load(fileobject)
        return data

class JSONWriter(BaseWriter):
    def __init__(self, data):
        self.data = data

    def write(self, fileobject):
        json.dump(self.data, fileobject)

class TXTReader(BaseReader):
    def read(self, fileobject):
        data = fileobject.read()
        return data

class TXTWriter(BaseWriter):
    def __init__(self, data):
        self.data = data

    def write(self, fileobject):
        fileobject.write(self.data)
        
def read_data(fileobj, reader: BaseReader):
    r = reader()
    return r.read(fileobj)

def dump_data(data, fileobj, writer: BaseWriter):
    w = writer(data)
    return w.write(fileobj)

print()