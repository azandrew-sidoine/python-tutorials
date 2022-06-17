
def main():
    source = range(1, 10)
    def square(x): return x**2
    output = map_func(square, source)
    print(f"Source : {' '.join(map_func(str, source))}")
    print(f"Output : {' '.join(map_func(str, output))}")
    print(f"Output : {filter_func(lambda x : x%2==0, output)}")

    rev_list = list(range(10, 1, -1))
    rev_list.append(3)
    rev_list.append(3)
    rev_list.append(4)
    print('Set = {}'.format(list(set(rev_list))))

    # Les énumerables
    for index, value in enumerate(['apple', 'banana', 'mango']):
        print([index, value])

    # Combinaison de 2 liste
    print('**Combinaison**')
    for value1, value2 in zip([1, 2, 3], ['apple', 'banana', 'mango']):
        print([value1, value2])


# List comprehension
# [<valeur_de_rretour> <boucle> <condition>] -> Note: La condition n'est pas toujours requis
# L'operateur {} crée plutôt une compréhension de dictionnaire
def map_func(func: callable, source: list):
    # output = []
    # for item in source:
    #     output.append(func(item))
    # return output
    return [func(item) for item in source]


def filter_func(func: callable, source: list):
    # output = []
    # for item in source:
    #   if True == func(item):
    #     output.append(item)
    # return output
    return [x for x in source if True == func(x)]


if __name__ == '__main__':
    main()
