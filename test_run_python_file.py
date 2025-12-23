from functions.run_python_file import run_python_file


def test_run_cases():
    r1 = run_python_file("calculator", "main.py")
    print(r1)
    assert ("Usage:" in r1) or ("Calculator App" in r1)

    r2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(r2)
    assert "STDOUT" in r2 or "Process exited" in r2

    r3 = run_python_file("calculator", "tests.py")
    print(r3)
    assert ("OK" in r3) or ("Process exited with code" in r3) or ("STDOUT" in r3)

    r4 = run_python_file("calculator", "../main.py")
    print(r4)
    assert r4.startswith('Error:')

    r5 = run_python_file("calculator", "nonexistent.py")
    print(r5)
    assert r5.startswith('Error:')

    r6 = run_python_file("calculator", "lorem.txt")
    print(r6)
    assert r6.startswith('Error:')


if __name__ == "__main__":
    test_run_cases()
