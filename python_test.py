import json
import random


def main() -> (dict, dict, dict, dict, ):
    # NOTE: Get all the parse commands
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    parse_commands = []
    copy_commands = []
    random_commands = []

    for row in data:
        if 'function' in row and row['function'] == 'parse':
            parse_commands.append(row.copy())
        elif 'function' in row and row['function'] == 'copy':
            copy_commands.append(row.copy())
        random_commands = random.sample(data, 2)
    # print(f"random_commands: {random_commands}")
    # print(f"parse_commands: {parse_commands}")
    # print(f"copy_commands: {copy_commands}")

    # General function for adding parse as well copy commands etc
    def addingGeneral(row,type, counter) -> (dict) :
        new_row= row.copy()
        new_row['_list'] = type
        new_row['_counter'] = counter
        return  new_row

    # List compression
    functional_commands = [addingGeneral(row,'parse',i) for i,row in  enumerate(parse_commands, 1)]
    functional_commands.extend([addingGeneral(row,'copy',i) for i,row in  enumerate(copy_commands, 1)])
    # print(f"functional_commands: {functional_commands}")


    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
