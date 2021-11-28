import csv
import collections
import json
import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = collections.defaultdict(set)
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            routes[line[2]].add(line[4])
    return routes

def find_paths(routes, source, dest, max_segments):
    frontier = {source}
    seen = {source: {(source,)}}

    for steps in range(max_segments):
        new_frontier = set()
        for next in frontier:
            for target in routes.get(next, ()):
                if target not in seen:
                    seen[target] = set()
                    new_frontier.add(target)
                pass
                for path in seen[next]:
                    if len(path) != steps + 1:
                        continue
                    seen[target].add(path + (target,))
        frontier = new_frontier

    return seen[dest]

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    paths_clear_names = list(map(lambda path : list(map(lambda elem :  airports.get(elem), path)), paths))

    result = collections.defaultdict(list)
    for path in paths_clear_names:
        result[len(path)-1].append(path)
    print(json.dumps(result, indent=4, sort_keys=True))
    
    # Don't forget to write the output to JSON!

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
