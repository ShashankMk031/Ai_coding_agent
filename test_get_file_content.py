from functions.get_file_content import get_file_content


def test_lorem_truncation():
    content = get_file_content("calculator", "lorem.txt")
    assert isinstance(content, str)
    # Should include truncation message
    assert f'truncated at 10000 characters' in content
    # Content should be longer than the MAX_CHARS because of the appended message
    assert len(content) > 10000


def test_print_cases():
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    test_lorem_truncation()
    test_print_cases()
