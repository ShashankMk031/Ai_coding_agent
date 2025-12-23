from functions.write_file import write_file
import os


def test_write_cases():
    # Overwrite existing lorem.txt
    res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(res1)

    # Create a new file inside calculator/pkg
    res2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(res2)

    # Attempt to write outside working directory
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(res3)

    # Basic assertions
    assert res1.startswith('Successfully wrote') or res1.startswith('Error:')
    assert res2.startswith('Successfully wrote')
    assert res3.startswith('Error:')


if __name__ == "__main__":
    test_write_cases()
