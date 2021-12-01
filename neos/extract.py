"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.1
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    result = []
    with open(neo_csv_path) as neo_file:
        reader = csv.DictReader(neo_file)
        for line in reader:
            result.append(NearEarthObject(
                line['pdes'],
                line['name'] if line['name'] else None,
                float(line['diameter']) if line['diameter'] else float('nan'),
                line['pha'] == 'Y',
            ))
    print(f"Loaded {len(result)} NEOs")
    return result


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    result = []
    with open(cad_json_path) as cad_file:
        cad_json = json.load(cad_file)
        total = len(cad_json['data'])
        percent = int(total / 100)
        print(f"Loading {total} CloseApproaches:")
        current = 0
        for cad in cad_json['data']:
            result.append(CloseApproach(
                designation=cad[0],
                time=cad[3],
                distance=float(cad[4]),
                velocity=float(cad[7]),
            ))
            if current % percent == 0:
                printProgressBar(current, total)
            current += 1
        printProgressBar(100, 100)
    print("Done.")
    return result


# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar (iteration, total, prefix='', suffix='', decimals=1,
                      length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : pos. number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}")\
        .format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
