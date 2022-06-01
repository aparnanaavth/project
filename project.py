import re

class Assessment:

    '''
    
    '''
    def read_file(self, directory, file_name):
        file = open(f'{directory}/{file_name}', 'r')
        lines = file.readlines()
        file.close()
        return lines

    def write_file(self, directory, file_name, lines):
        file = open(f'{directory}/{file_name}', 'w')
        for line in lines:
            file.write(line)
        file.close()
    
    def filter_duplicates(self, lines):
        seen = set()
        data = ''
        for line in lines:
            line = line.replace(';', ',')
            if line.find(',,') != -1: continue
            if line not in seen:
                seen.add(line)
                data += line
        return data

    def average(self, lines):
        data = ''
        data += lines[0]
        for line in lines:
            field = line.split(',')
            if re.search('^A',field[0]) is not None:
                data += line
        return data


obj = Assessment()
file1 = obj.read_file('data', 'factbook.csv')
file2 = obj.read_file('data', 'factbook-2.csv')
data = obj.filter_duplicates(file1 + file2)
obj.write_file('temp', 'temp.csv', data)
data = obj.average(obj.read_file('temp', 'temp.csv'))
obj.write_file('output', 'output.csv', data)