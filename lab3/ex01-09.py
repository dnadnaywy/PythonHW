def ex01(a: list, b: list) -> list:
    set_a = set(a)
    set_b = set(b)
    list_of_sets = []

    intersection = set_a & set_b
    list_of_sets.append(intersection)

    union = set_a | set_b
    list_of_sets.append(union)

    a_b = set_a - set_b
    list_of_sets.append(a_b)

    b_a = set_b - set_a
    list_of_sets.append(b_a)

    return list_of_sets


# print(ex01([1, 2, 3, 5, 9, 9], [2, 2, 4, 5, 9]))

def ex02(text: str) -> dict:
    letters = {}
    for char in text:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] = letters[char] + 1
    return letters


# print(ex02("Ana has apples."))

def ex03(dict1: dict, dict2: dict) -> bool:
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        for key in dict1:
            if not ex03(dict1[key], dict2[key]):
                return False
        return True

    elif isinstance(dict1, (list, set)):
        if len(dict1) != len(dict2):
            return False

        for elem1, elem2 in zip(sorted(dict1), sorted(dict2)):
            if not ex03(elem1, elem2):
                return False
        return True

    return dict1 == dict2


dict1 = {'a': 1, 'b': {'x': 1, 'y': [1, 2]}}
dict2 = {'a': 1, 'b': {'x': 1, 'y': [1, 2]}}


# print(ex03(dict1, dict2))

def ex04_build_xml_element(tag, content, **dict) -> str:
    string_from_dictionary = ""
    for key, value in dict.items():
        string_from_dictionary += key + "=\"" + value + "\ \""

    string = "<" + tag + " " + string_from_dictionary + "> " + content + " </" + tag + ">"
    return string


# print(ex04_build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

# TODO: ex5
def ex05_validate_dict(tuples: set, dictio: dict) -> bool:
    for key, value in dictio.items():
        for tuple in tuples:
            if key not in tuple:
                return False
            else:
                if value.startswith(tuple[1]) == False:
                    return False
                if value.endswith(tuple[3]) == False:
                    return False
                if tuple[2] not in value:
                    return False
                break
    return True


print(ex05_validate_dict({("key1", "c", "inside", ""), ("key2", "start", "middle", "winter")},
                         {"key1": "come inside, it's too cold out"}))
# print(ex05_validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#                          {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))

def ex06(lista: list) -> tuple:
    unique = set(lista)
    result = (len(unique), len(lista) - len(unique))
    return result


# print(ex06([1, 2, 3, 3, 2, 4, 4]))

def ex07(*sets) -> dict:
    result = {}
    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            string = str(set1) + " | " + str(set2)
            if string not in result:
                result[string] = set1 | set2

            string = str(set1) + " & " + str(set2)
            if string not in result:
                result[string] = set1 & set2

            string = str(set1) + " - " + str(set2)
            if string not in result:
                result[string] = set1 - set2

            string = str(set2) + " - " + str(set1)
            if string not in result:
                result[string] = set2 - set1

    return result


# print(ex07({1, 2}, {2, 3}, {3, 4}))

def ex08(mapping: dict) -> list:
    result = []
    step = mapping["start"]
    # print(step)

    while (step not in result):
        result.append(step)
        step = mapping[step]

    return result


# print(ex08({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

def ex09(*arg, **keyword_arg) -> int:
    contor = 0
    for key, value in keyword_arg.items():
        if value in arg:
            contor += 1
    return contor

# print(ex09(1, 2, 3, 4, x=1, y=2, z=3, w=5))
