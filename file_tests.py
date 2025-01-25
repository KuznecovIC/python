from file_classes import JsonFile, TxtFile, CsvFile

def test_json_file():
    json_file = JsonFile('data.json')
    json_file.write({"name": "John", "age": 30})
    print("JSON Read:", json_file.read())
    json_file.append({"city": "New York"})
    print("JSON After Append:", json_file.read())

def test_txt_file():
    txt_file = TxtFile('data.txt')
    txt_file.write("Hello, world!\n")
    print("TXT Read:", txt_file.read())
    txt_file.append("Appended text.")
    print("TXT After Append:", txt_file.read())

def test_csv_file():
    csv_file = CsvFile('data.csv')
    csv_file.write([["name", "age"], ["John", 30]])
    print("CSV Read:", csv_file.read())
    csv_file.append([["Alice", 25]])
    print("CSV After Append:", csv_file.read())

if __name__ == "__main__":
    test_json_file()
    test_txt_file()
    test_csv_file()