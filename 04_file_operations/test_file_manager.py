from file_manager import FileManager
import pytest
import os

def test_read_file():
    """Test reading a file."""
    file_path = 'test_file.txt'
    content = 'Hello, World!'

    with open(file_path, 'w') as file:
        file.write(content)
    assert FileManager.read_file(file_path) == content

    with pytest.raises(FileNotFoundError):
        FileManager.read_file('non_existent_file.txt')

def test_delete_file():
    file_path = 'test_file.txt'
    FileManager.delete_file(file_path)
    assert not os.path.exists(file_path)

def test_write_file():
    """Test writing to a file."""
    file_path = 'write_test.txt'
    content = 'This is a test.'

    FileManager.write_file(file_path, content)
    assert FileManager.read_file(file_path) == content

    """Clean up the test file."""
    FileManager.delete_file(file_path)

def test_append_to_file():
    """Test appending to a file."""
    file_path = 'append_test.txt'
    initial_content = 'Initial content.'
    append_content = ' Appended content.'

    FileManager.write_file(file_path, initial_content)
    FileManager.append_to_file(file_path, append_content)
    
    assert FileManager.read_file(file_path) == initial_content + append_content

    """Clean up the test file."""
    FileManager.delete_file(file_path)

def test_is_exists():
    """Test checking if a file exists."""
    file_path = 'exists_test.txt'
    
    FileManager.write_file(file_path, 'Test content.')
    assert FileManager.is_exists(file_path) is True
    
    FileManager.delete_file(file_path)
    assert FileManager.is_exists(file_path) is False

def test_create_directory():
    """Test creating a directory."""
    dir_path = 'test_directory'
    
    FileManager.create_directory(dir_path)
    assert os.path.exists(dir_path) is True

def test_delete_directory():
    """Test deleting a directory."""
    dir_path = 'test_directory'

    FileManager.delete_directory(dir_path)
    assert os.path.exists(dir_path) is False

def test_size_of_file():
    """Test getting the size of a file."""
    file_path = 'size_test.txt'
    content = 'This is a test for file size.'

    FileManager.write_file(file_path, content)
    assert FileManager.size_of_file(file_path) == len(content)

    FileManager.delete_file(file_path)
    
    with pytest.raises(FileNotFoundError):
        FileManager.size_of_file(file_path)

def test_size_of_directory():
    """Test getting the size of a directory."""
    dir_path = 'size_test_directory'
    FileManager.create_directory(dir_path)
    
    # Create a file in the directory
    fisrt_file_path = os.path.join(dir_path, 'test_file1.txt')
    second_file_path = os.path.join(dir_path, 'test_file2.txt')
    content = 'File in directory.'
    FileManager.write_file(fisrt_file_path, content)
    FileManager.write_file(second_file_path, content)
    
    # Check the size of the file
    assert FileManager.size_of_directory(dir_path) == len(content) * 2  # Two files with the same content

    # Clean up
    FileManager.delete_directory(dir_path)

def test_list_files_in_directory():
    """Test listing files in a directory."""
    dir_path = 'list_test_directory'
    FileManager.create_directory(dir_path)
    
    # Create some files in the directory
    file1 = os.path.join(dir_path, 'file1.txt')
    file2 = os.path.join(dir_path, 'file2.txt')
    FileManager.write_file(file1, 'Content of file 1.')
    FileManager.write_file(file2, 'Content of file 2.')
    
    files = FileManager.list_files_in_directory(dir_path)
    assert set(files) == {os.path.basename(file1), os.path.basename(file2)}

    # Clean up
    FileManager.delete_directory(dir_path)

def test_copy_file():
    """Test copying a file."""
    source_file = 'source_file.txt'
    destination_file = 'destination_file.txt'
    content = 'This is a test for file copy.'

    FileManager.write_file(source_file, content)
    FileManager.copy_file(source_file, destination_file)

    assert FileManager.read_file(destination_file) == content

    # Clean up
    FileManager.delete_file(source_file)
    FileManager.delete_file(destination_file)

def test_move_file():
    """Test moving a file."""
    source_file = 'move_source.txt'
    destination_file = 'move_destination.txt'
    content = 'This is a test for file move.'

    FileManager.write_file(source_file, content)
    FileManager.move_file(source_file, destination_file)

    assert FileManager.read_file(destination_file) == content

    # Clean up
    FileManager.delete_file(destination_file)

def test_rename_file():
    """Test renaming a file."""
    original_file = 'rename_original.txt'
    renamed_file = 'rename_new.txt'
    content = 'This is a test for file rename.'

    FileManager.write_file(original_file, content)
    FileManager.rename_file(original_file, renamed_file)

    assert FileManager.read_file(renamed_file) == content

    # Clean up
    FileManager.delete_file(renamed_file)

def test_search_file_like():
    """Test searching for files matching a pattern."""
    dir_path = 'search_test_directory'
    FileManager.create_directory(dir_path)
    
    # Створюємо файли з різними іменами
    file1 = os.path.join(dir_path, 'test_file.txt')
    file2 = os.path.join(dir_path, 'example.txt') 
    file3 = os.path.join(dir_path, 'test_data.csv')
    
    FileManager.write_file(file1, 'content')
    FileManager.write_file(file2, 'content')
    FileManager.write_file(file3, 'content')
    
    # Шукаємо файли з "test" у назві
    matching_files = FileManager.search_file_like(dir_path, 'test')
    assert len(matching_files) == 2
    assert matching_files == ['search_test_directory\\test_data.csv', 'search_test_directory\\test_file.txt']
    
    # Clean up
    FileManager.delete_directory(dir_path)