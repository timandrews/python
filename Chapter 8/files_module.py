#!/usr/bin/python3



def openFiles():
    
    smoking_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4

    while(not smoking_datafile_opened or not cancer_datafile_opened) and (num_attempts > 0):
        try:
            if not smoking_datafile_opened:
                file_name = input('Enter smoking date file name:  ')
                smoking_datafile = open(file_name, 'r')
                smoking_datafile_opened = True

            if not cancer_datafile_opened:
                file_name = input('Enter cancer data file name:  ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True

        except IOError:
            print('File "', file_name, '" not opened.  Please try again')
            num_attempts = num_attempts - 1

    if not smoking_datafile_opened or not cancer_datafile_opened:
        raise IOError
    else:
        return (smoking_datafile, cancer_datafile)

def readFiles(smoking_datafile, cancer_datafile):
    smoking_data = []
    cancer_data = []
    empty_str = ''

    smoking_datafile.readline()
    cancer_datafile.readline()

    eof = False

    while not eof:
        smoke_line = smoking_datafile.readline()
        cancer_line = cancer_datafile.readline()

        if smoke_line == empty_str and cancer_line == empty_str:
            eof = True
        elif smoke_line == empty_str:
            raise IOError ('Unexpected end of file :  smoking data file')
        elif cancer_line == empty_str:
            raise IOError('Unexpected end of file : cancer data file')
        else:
            smoking_data.append(smoke_line.strip().split(','))
            print('smoking number:  ' , smoke_line)
            cancer_data.append(cancer_line.strip().split(','))
            print('cancer numbers; ', cancer_line)
    return (smoking_data, cancer_data)

    
