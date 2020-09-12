'''
This will cover reading and writing files with CSV and JSON files
'''
import csv, os


#opening and reading a file
example_file = open ("example.csv")
example_reader = csv.reader(example_file)   
#example_data = list(example_reader)            # easy way to read as list and access a specific value
                                                # to not overflow memory it is generally better to put this in a for loop
                                                # CAN ONLY BE LOOPED OVER ONCE (else create a new reader Object)
#print (example_data)                            
for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))
example_file.close()


#creating a new file and writing to it
if not os.path.exists("output.csv"):
    output_file = open ("output.csv","w",newline ="")                   # pretty much similar to just opening any plaintext file
    output_writer = csv.writer(output_file)
    output_writer.writerow(['I','like','dem','apples',', do you?'])
    output_file.close()
else:
    print ("output.csv already exists in cwd")


# delimiter and lineterminator (layout)
if not os.path.exists("tab_example.tsv"):
    tab_example_file = open("tab_example.tsv", "w", newline="")                                     # csv = comma seperated values | tsv = tab seperated values
    tab_example_writer = csv.writer(tab_example_file, delimiter = "\t", lineterminator = "\n\n")
    tab_example_writer.writerow(['I','like','dem','apples',', do you?'])
    tab_example_writer.writerow(["In","deed", "I","do", ", Sir"])
else:
    print ("tab_example.tsv already exists in cwd")


# working with header-rows: DictReader and DictWriter
# takes header (first row) and uses it as keys for all values under it
# you can add values to a key or extract them from it