"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import helpers


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writerow(dict(zip(fieldnames, fieldnames)))
        for result in results:
            approach_data = (helpers.datetime_to_str(result.time), result.distance, result.velocity, result.neo.designation, result.neo.name, result.neo.diameter, result.neo.hazardous)
            writer.writerow(dict(zip(fieldnames, approach_data)))


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'neo')
    fieldnames_neo = ('designation', 'name', 'diameter_km', 'potentially_hazardous',)
    output = []
    for result in results:
        neo_data = (result.neo.designation, result.neo.name, result.neo.diameter, result.neo.hazardous)
        neo_dict = dict(zip(fieldnames_neo, neo_data))
        approach_data = (helpers.datetime_to_str(result.time), result.distance, result.velocity, neo_dict)
        approach_dict = dict(zip(fieldnames, approach_data))
        output.append(approach_dict)
    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)