
from utils import io

class DirElement:
    def __init__(self, name:str, size:int=None):

        if size is not None and int(size) == 0:
            raise ValueError('Unexpected file size of 0')

        self.name = name
        self.parent = None
        self._size = int(size) if size is not None else None
        self._content = []

    def get_dirs(self, name):
        if not self.is_dir():
            raise NotImplementedError(f"Cannot perform such action for non dir {self!r}")

        return [element for element in self._content if element.is_dir()]

    def get_dir(self, name):
        if not self.is_dir():
            raise NotImplementedError(f"Cannot perform such action for non dir {self!r}")

        for dir_element in self._content:
            if dir_element.is_dir() and dir_element.name == name:
                return dir_element

        return None


    def update_parent(self, dir_element):
        self.parent = dir_element

    def is_dir(self):
        return not bool(self._size)

    def is_file(self):
        return bool(self._size)

    @property
    def content(self):
        return self._content

    @property
    def size(self):
        if self.is_file():
            return self._size
        else:
            return sum([element.size for element in self._content])

    def add_element(self, element):
        if self.is_file():
            raise ValueError(f'{self!r} cannot add {element}' )

        self._content.append(element)
        element.update_parent(self)

    def __str__(self):
        return f"Element [{'dir' if self.is_dir() else 'file'}] {self.name!r}"

def parse_dir_output(dir_content:list, root_dir:DirElement):
    for content_description in dir_content:
        match content_description.split():
            case ["dir", element_name]:
                root_dir.add_element(DirElement(element_name))
            case [size, element_name]:
                root_dir.add_element(DirElement(element_name, size))

def parse_commmand(current_dir:DirElement, terminal_line: str):

    match terminal_line.split():
        case["$", "cd", ".."]:
            return current_dir.parent
        case ["$", "cd", dir_name]:
            return current_dir.get_dir(dir_name)
        case ["$", "ls"]:
            return current_dir
        case ["dir", element_name]:
            current_dir.add_element(DirElement(element_name))
            return current_dir
        case [size, element_name]:
            current_dir.add_element(DirElement(element_name, size))
            return current_dir

def display_element(element_dir: DirElement, indent=0):
    print(f"{'    ' * indent} - {element_dir}")

    if element_dir.is_dir():
        for item in element_dir.content:
            display_element(item, indent + 1)

def collect_top_dirs(element_dir: DirElement, elements):
    if element_dir.is_dir():
        if element_dir.size <= 100_000:
            elements.append(element_dir)
        for item in element_dir.content:
            collect_top_dirs(item, elements)

def lookup_min_dir(dir_element:DirElement):
    global min_dir
    if dir_element.is_dir() and dir_element.size > missing_space:
        if min_dir is None:
            min_dir = dir_element
        elif min_dir.size > dir_element.size:
            min_dir = dir_element

        for item in dir_element.content:
            lookup_min_dir(item)

if __name__ == "__main__":
    root_dir = None
    current_dir = None

    input_reader = io.load_game_input()

    first_line = next(input_reader)
    if first_line == '$ cd /':
        root_dir = DirElement("/")
        current_dir = root_dir
    else:
        raise ValueError('My lazy implementation starts only from root')


    for line in input_reader:
        current_dir = parse_commmand(current_dir, line)


    display_element(root_dir)

    top_elements = []
    collect_top_dirs(root_dir, top_elements)

    print(sum(element.size for element in top_elements))

    TOTAL_AVAILABLE_SIZE = 70000000
    REQUIRED_SPACE = 30000000
    missing_space = REQUIRED_SPACE - (TOTAL_AVAILABLE_SIZE - root_dir.size)

    print(f"Current free space : {TOTAL_AVAILABLE_SIZE - root_dir.size}, missing {missing_space}")

    min_dir = None

    lookup_min_dir(root_dir)
    print(min_dir.size)
