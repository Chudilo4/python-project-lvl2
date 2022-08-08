from package.gendiff import generate_diff


def test_generate_diff():
    assert generate_diff('tests/file1.json', 'tests/file2.json') == str({
        - follow: false
          host: hexlet.io
        - proxy: 123.234.53.22
        - timeout: 50
        + timeout: 20
        + verbose: true
        })
                    
