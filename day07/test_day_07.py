import pytest

import day07.day_07 as d7

def test_dir_creation():
    de = d7.DirElement("a")
    assert de.is_dir()
    assert not de.is_file()
    assert de.name == "a"
    assert de.size == 0

def test_file_creation():
    de = d7.DirElement("b.txt", 14848514)
    assert de.is_file()
    assert not de.is_dir()
    assert de.name == 'b.txt'
    assert de.size == 14848514

def test_file_should_not_add_element():
    de = d7.DirElement("b.txt", 14848514)
    with pytest.raises(ValueError):
        de.add_element(d7.DirElement('Test'))

def test_dir_with_elements():
    de_dir = d7.DirElement("a")
    de_f1 = d7.DirElement("b.txt", 14848514)
    de_f2 = d7.DirElement("c.dat", 8504156)

    de_dir.add_element(de_f1)
    de_dir.add_element(de_f2)

    assert de_dir.size == 23352670
    assert de_f1.parent == de_dir


def test_parse_dir_output():
    test_dir_content = ["dir a", "14848514 b.txt", "8504156 c.dat", "dir d"]
    dir_root = d7.DirElement('root')
    d7.parse_dir_output(test_dir_content, dir_root)
    assert dir_root.size == 23352670
    assert len(dir_root._content) == 4


test_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

