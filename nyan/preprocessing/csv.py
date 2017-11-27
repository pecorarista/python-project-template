from nyan.cat import Cat, Sexes


def read_csv(filename, delimiter='\t'):
    """Read CSV
    Args:
        filename (str)
        delimiter (str)
    Returns:
        list(nyan.Cat)
    """

    results = []

    with open(filename, mode='r') as f:
        for line in f:
            fields = line.strip().split(delimiter)

            try:
                sex = Sexes(fields[3])
            except ValueError:
                sex = Sexes('others')

            cat = Cat(name=fields[0],
                      breed=fields[1],
                      age=int(fields[2]),
                      sex=sex)
            results.append(cat)

    return results
