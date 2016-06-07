import csv

MY_FILE = '../data/sample.csv'

def parse(raw_file, delimeter):
""" parse a raw CSV file to a JSON-line object """

    # open csv file
    opened_file = open(raw_file)

    # read csv file
    csv_data = csv.reader(opened_file, delimeter=delimeter)

    # build data structure
    parsed_data = []

    fields = csv_data.next()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # close csv file
    opened_file.close()

    # return parsed data as data structure
    return parsed_data


def main():
    new_data = parse(MY_FILE, ",")

    # print data
    print   new_data
