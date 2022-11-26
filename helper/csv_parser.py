from dataclass_csv import DataclassReader


class CsvParser:
    def __init__(self, file_path: str, clazz):
        self.csv_data = []

        with open(file_path, 'rt') as csv_file:
            reader = DataclassReader(csv_file, clazz)

            for row in reader:
                self.csv_data.append(row)

    def filter_on_test_case_id(self, test_case_id: str) -> list:
        data_list = [row for row in self.csv_data if row.test_case_id == test_case_id]

        return data_list
