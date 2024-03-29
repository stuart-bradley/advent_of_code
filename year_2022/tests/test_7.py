import pytest
from year_2022.challenge_7.module import directory_size, directory_to_delete


@pytest.fixture
def commands():
    raw_input = """$ cd /
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
7214296 k"""
    return raw_input.splitlines()


def test_file_size(commands):
    assert directory_size(commands) == 95437


def test_directory_to_delete(commands):
    assert directory_to_delete(commands) == 24933642
