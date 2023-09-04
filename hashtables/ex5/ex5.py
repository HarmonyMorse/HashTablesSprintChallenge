def finder(files, queries):
    table = {}
    result = []

    for path in files:
        slash = path.rfind("/")
        file_name = path[slash + 1:]
        if file_name in table:
            table[file_name].append(path)
        else:
            table[file_name] = [path]
    for query in queries:
        if query in table:
            for res in table[query]:
                result.append(res)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
