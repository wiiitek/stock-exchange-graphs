import csv


def _save_to_csv(filename: str, currency_rates: tuple):
    with open(filename, mode='w+') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=',',
                            lineterminator='\n',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

        for item in currency_rates:
            writer.writerow([item[0], item[1]])
        csv_file.close()
