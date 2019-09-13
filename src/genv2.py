import os
import csv
import time

d = 'openaddr-collected-us/us'

dirs = os.listdir(d)
big_dict = {}
state_directory = 'md'

start = time.time()
for subdir, dirs, files in os.walk(d + '/' + state_directory):
  for file in files:
    file_path = d + '/' + state_directory + '/' + file
    print(file_path)
    with open(file_path, 'r') as csvFile:
      readCSV = csv.reader(csvFile, delimiter=',')
      filename, file_extension = os.path.splitext(file_path)
      iterated_cities = []
      next(csvFile)
      for row in readCSV:
        print(row)
        if(row[5] in iterated_cities):
          print("City has already been parsed")
          continue
        else:
          big_dict[state_directory.upper()] = {row[5]: [csvRow[3] for csvRow in readCSV if csvRow[5] == 'BUNNELL']}
        iterated_cities.append(row[5])
end = time.time()  


print(big_dict)
print(end - start)