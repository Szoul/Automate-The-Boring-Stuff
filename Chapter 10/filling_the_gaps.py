#! python 3.8.3
# filling_the_gaps.py - find gaps within the numbering of similar files in a directory
# 2nd task - insert a gap in between two files of such a directory at a given potition

# TODO (find gaps)
        # assuming input: prefix, suffix, Path-Object of the directory to search
        # assuming: files can lie within subfolders
        # assuming: all files have the exact same wording (and suffix) except for the number
        # assuming: files are numbered, beginning from 001 up to 999

    # find files with given prefix/suffix in a directory
        # regex to match files
    # check if any numbers are missing
        # iterate through every file
        # check if any number in a number row is missing
            # make a list of numbers of the folder
                # that list would make it easy to check if any number was used twice by accident
            # iterate x times, x being the highest number in the list
            # check if a number not in number_of_list
    # print(return) out the missing filenames/numbers

def find_gaps(prefix, suffix, directory_path):
    import re, os
    from pathlib import Path

    regex = re.compile(rf"""
                        ^{prefix}
                        (\d\d[1-9])
                        \.{suffix}$
                        """, re.VERBOSE)
    
    list_of_filenumbers = []

    for folders, subfolders, files in os.walk(directory_path):
        for filename in files:
            match = regex.search(filename)
            if match != None:
                list_of_filenumbers.append(int(match.group(1)))

    highest_number = 0
    for i in list_of_filenumbers:
        if i > highest_number:
            highest_number = i
    
    list_of_missing_numbers = []
    for number in range (1, highest_number):
        if number not in list_of_filenumbers:
            if number < 10:
                str_number = "00" + str(number)
            elif number < 100:
                str_number = "0" + str(number)
            else:
                str_number = str(number)
            list_of_missing_numbers.append(str_number)
    
    if len(list_of_missing_numbers) != 0:
        print ("The files in this folders are incomplete. Following file(s) are missing:")
        for missing_number in list_of_missing_numbers:
            print (str(prefix) + missing_number + "." + suffix)
    else:
        print ("There are no files missing")

    return list_of_missing_numbers





# TODO (make gap)
        # assuming the same things as with the find gaps function
        # assume that there is no gap yet
    # input (filename) for number where gap should be
    # increase the number of every file with the input-number or greater by one
        # rename them with shutil.move()
    # print out the name of the file that is now missing

def make_gap (filename, directory_path):
    import re, os, shutil
    from pathlib import Path

    if (Path(f"{directory_path}/{filename}")).exists():
        pass
    else:
        print (f"{filename} does not exist within {directory_path}")
        return

    file_regex = re.compile(r"""
                            (^.*?)                      #prefix
                            (\d\d[1-9])                 #number from 001-999
                            \.                          #dot    
                            (.*?$)                      #suffix
                            """, re.VERBOSE)
    
    file_name = filename
    file_nmb = file_regex.search(filename)
    prefix = file_nmb.group(1)
    gap_number = file_nmb.group(2)
    suffix = file_nmb.group(3)

    regex = re.compile(rf"""
                        ^{prefix}
                        (\d\d[1-9])
                        \.{suffix}$
                        """, re.VERBOSE)

    for folders, subfolders, files in os.walk(directory_path):
        for filename in files:
            match = regex.search(filename)
            print (filename)
            if match != None:
                if int(match.group(1)) >= int(gap_number):
                    folders = folders.replace("\\", "/")
                    file_path = Path(f"{folders}/{filename}")
                    new_nmb = int(match.group(1)) + 1
                    if new_nmb < 10:
                        str_number = "00" + str(new_nmb)
                    elif new_nmb < 100:
                        str_number = "0" + str(new_nmb)
                    else:
                        str_number = str(new_nmb)

                    new_filename = f"{prefix}{str_number}.{suffix}"
                    new_filepath = Path(f"{folders}/{new_filename}")

                    #print (file_path)
                    #print (new_filepath)
                    #print ("___________________________")
                    shutil.move(file_path, new_filepath)

    print (f"{file_name}, and any file with a greater number has been moved up by one. There is now a gap where {file_name} was.")



from pathlib import Path
test_folder = Path("C:/Users/Acer PC/Desktop/Python/Automate-The-Boring-Stuff/Chapter 10/filling_the_gaps_test")

x = find_gaps("test", "txt", test_folder)
print (x)
print ("\n\n")

make_gap("test006.txt", test_folder)