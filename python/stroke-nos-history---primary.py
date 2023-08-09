# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"ZV12511","system":"readv2"},{"code":"ZV12512","system":"readv2"},{"code":"100639.0","system":"med"},{"code":"104505.0","system":"med"},{"code":"104638.0","system":"med"},{"code":"105100.0","system":"med"},{"code":"107195.0","system":"med"},{"code":"107886.0","system":"med"},{"code":"10792.0","system":"med"},{"code":"10962.0","system":"med"},{"code":"109743.0","system":"med"},{"code":"110337.0","system":"med"},{"code":"11039.0","system":"med"},{"code":"11074.0","system":"med"},{"code":"18686.0","system":"med"},{"code":"19348.0","system":"med"},{"code":"34135.0","system":"med"},{"code":"55351.0","system":"med"},{"code":"56458.0","system":"med"},{"code":"5871.0","system":"med"},{"code":"6228.0","system":"med"},{"code":"6305.0","system":"med"},{"code":"66873.0","system":"med"},{"code":"7138.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-nos-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke-nos-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke-nos-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke-nos-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
