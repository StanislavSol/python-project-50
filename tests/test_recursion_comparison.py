from gendiff.parser import get_decoder_data
from gendiff.diff import generate_diff
from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
LAST_ELEMENT = -1


def get_files_with_recursion_yaml():
    path_file1 = 'tests/fixtures/recursive_data_yml/file1.yaml'
    path_file2 = 'tests/fixtures/recursive_data_yml/file2.yaml'
    path_sample_file = 'tests/fixtures/recursive_data_yml/sample_output_recursion.yaml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def get_files_with_recursion_json():
    path_file1 = 'tests/fixtures/recursive_data_json/file1.json'
    path_file2 = 'tests/fixtures/recursive_data_json/file2.json'
    path_sample_file = 'tests/fixtures/recursive_data_json/sample_output_recursion.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def get_files_json():
    path_file1 = 'tests/fixtures/flat_data_json/file1.json'
    path_file2 = 'tests/fixtures/flat_data_json/file2.json'
    path_sample_file = 'tests/fixtures/flat_data_json/sample_output.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def get_files_yaml():
    path_file1 = 'tests/fixtures/flat_data_yml/file1.yml'
    path_file2 = 'tests/fixtures/flat_data_yml/file2.yml'
    path_sample_file = 'tests/fixtures/flat_data_yml/sample_output.yml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()



def test_generate_diff():
    files_for_test = (
                       get_files_yaml(),
                       get_files_json(),
                       get_files_with_recursion_json(),
                       get_files_with_recursion_yaml()
                       )
    for files in files_for_test:
        parsed_dict = get_decoder_data(*files[:LAST_ELEMENT])
        result_data = generate_diff(*parsed_dict)
        verification_file = files[LAST_ELEMENT]
        assert get_stylish(result_data) == verification_file


def test_flat_diff():
    parsed_dict = get_decoder_data(*get_files_with_recursion_json()[:LAST_ELEMENT])
    result_data = generate_diff(*parsed_dict)
    sample_file = open('tests/fixtures/sample_file.json', 'r').read().rstrip()
    verification_file = sample_file
    assert get_plain(result_data) == verification_file
