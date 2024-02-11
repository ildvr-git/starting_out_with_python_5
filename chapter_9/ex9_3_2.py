import ex9_3_1 as first

def main():
    read_string = first.read_file()
    inverterd_codes = {first.CODES.get(i, "'"):list(i)[0] for i in first.CODES}
    transformed_string = first.transform(read_string, inverterd_codes)
    print(transformed_string)

main()