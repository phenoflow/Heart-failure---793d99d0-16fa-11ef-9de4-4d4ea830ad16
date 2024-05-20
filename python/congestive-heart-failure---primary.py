# Carr E, Bendayan R, Bean D, OGallagher K, Pickles A, Stahl D, Zakeri R, Searle T, Shek A, Kraljevic Z, Teo J, Shah A, Dobson R, 2024.

import sys, csv, re

codes = [{"code":"426263006","system":"snomedct"},{"code":"42343007","system":"snomedct"},{"code":"10633002","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('heart-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["congestive-heart-failure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["congestive-heart-failure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["congestive-heart-failure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
