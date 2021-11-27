import json
import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename, mode="r") as file:
        content = json.load(file)
    return content

def check(prize, year, category):
    year_matches = year == prize['year'] if year else True
    category_matches = category == prize['category'] if category else True
    return year_matches and category_matches

def main(year, category):
    data = load_nobel_prizes()
    result = [prize for prize in data['prizes'] if check(prize, year, category)]
    print(result)

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)


# Solution:
def load_nobel_prizes_2(filename='prize.json'):
    with open(filename) as f:
        return json.load(f)

def main_2(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']

    for prize in prizes:
        if 'laureates' not in prize:
            continue
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue

        print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            print(f"{firstname} {surname}: {laureate['motivation']}")