# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14A7.12","system":"readv2"},{"code":"12833.0","system":"med"},{"code":"1298.0","system":"med"},{"code":"1469.0","system":"med"},{"code":"17322.0","system":"med"},{"code":"33499.0","system":"med"},{"code":"47607.0","system":"med"},{"code":"51767.0","system":"med"},{"code":"56279.0","system":"med"},{"code":"6116.0","system":"med"},{"code":"6253.0","system":"med"},{"code":"7780.0","system":"med"},{"code":"8443.0","system":"med"},{"code":"93459.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-nos-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
