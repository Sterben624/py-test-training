from custom_list import CustomList
import pytest

@pytest.fixture
def custom_list():
    """Fixture to create a CustomList instance."""
    return CustomList()

def test_add_item(custom_list):
    custom_list.add(1)
    assert len(custom_list.items) == 1
    assert custom_list.items[0] == 1

def test_add_item_at_index(custom_list):
    """Test adding an item at a specific index."""
    custom_list.add(1)
    custom_list.add_index(2, 0)
    assert len(custom_list.items) == 2
    assert custom_list.items[0] == 2
    with pytest.raises(IndexError):
        custom_list.add_index(3, 3)

def test_get_item_by_index(custom_list):
    """Test getting an item by index."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(3)
    
    assert custom_list.get_item_by_index(0) == 1
    assert custom_list.get_item_by_index(1) == 2
    assert custom_list.get_item_by_index(2) == 3
    
    with pytest.raises(IndexError):
        custom_list.get_item_by_index(-1)
    
    with pytest.raises(IndexError):
        custom_list.get_item_by_index(3)

def test_remove_item(custom_list):
    """Test removing an item by value and index."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(3)
    
    custom_list.remove(item=2)
    assert len(custom_list.items) == 2
    assert custom_list.items[0] == 1
    assert custom_list.items[1] == 3
    
    with pytest.raises(ValueError):
        custom_list.remove(4)
    
    custom_list.remove(index=0)
    assert len(custom_list.items) == 1
    assert custom_list.items[0] == 3
    
    with pytest.raises(IndexError):
        custom_list.remove(index=5)

def test_get_copy_list(custom_list):
    """Test getting a copy of the list."""
    custom_list.add(1)
    custom_list.add(2)
    copy_list = custom_list.get_copy_list()
    
    assert copy_list == [1, 2]
    assert copy_list is not custom_list.items

def test_get_length(custom_list):
    """Test getting the length of the list."""
    assert custom_list.get_length() == 0
    custom_list.add(1)
    assert custom_list.get_length() == 1
    custom_list.add(2)
    assert custom_list.get_length() == 2

def test_is_empty(custom_list):
    """Test checking if the list is empty."""
    assert custom_list.is_empty() is True
    custom_list.add(1)
    assert custom_list.is_empty() is False

def test_clear(custom_list):
    """Test clearing the list."""
    custom_list.add(1)
    custom_list.add(2)
    assert len(custom_list.items) == 2
    custom_list.clear()
    assert len(custom_list.items) == 0

def test_search_index_item(custom_list):
    """Test searching for an item and getting its index."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(3)
    
    assert custom_list.search_index_item(2) == 1
    assert custom_list.search_index_item(4) == -1

def test_is_has_item(custom_list):
    """Test checking if an item exists in the list."""
    custom_list.add(1)
    custom_list.add(2)
    
    assert custom_list.is_has_item(1) is True
    assert custom_list.is_has_item(3) is False
    assert custom_list.is_has_item(2) is True

def test_count_item(custom_list):
    """Test counting occurrences of an item in the list."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(1)
    
    assert custom_list.count_item(1) == 2
    assert custom_list.count_item(2) == 1
    assert custom_list.count_item(3) == 0

def test_reverse_list(custom_list):
    """Test reversing the list."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(3)
    
    custom_list.reverse()
    assert custom_list.items == [3, 2, 1]

def test_sort_list(custom_list):
    """Test sorting the list."""
    custom_list.add(3)
    custom_list.add(1)
    custom_list.add(2)
    
    custom_list.sort()
    assert custom_list.items == [1, 2, 3]
    
    custom_list.items.sort(reverse=True)
    assert custom_list.items == [3, 2, 1]

def test_get_sublist_in_range(custom_list):
    """Test getting a sublist in a specified range."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(3)
    custom_list.add(4)
    
    sublist = custom_list.get_sublist_in_range(1, 3)
    assert sublist == [2, 3]
    
    with pytest.raises(IndexError):
        custom_list.get_sublist_in_range(-1, 2)
    
    with pytest.raises(IndexError):
        custom_list.get_sublist_in_range(1, 5)

def test_merge(custom_list):
    """Test merging another CustomList into the current list."""
    custom_list.add(1)
    custom_list.add(2)
    
    other_list = CustomList()
    other_list.add(3)
    other_list.add(4)
    
    custom_list.merge(other_list)
    
    assert len(custom_list.items) == 4
    assert custom_list.items == [1, 2, 3, 4]
    
    empty_list = CustomList()
    custom_list.merge(empty_list)
    assert len(custom_list.items) == 4

def test_to_string(custom_list):
    """Test converting the list to a string representation."""
    custom_list.add(1)
    custom_list.add(2)
    custom_list.add(3)
    
    assert custom_list.to_string() == "[1, 2, 3]"
    
    custom_list.clear()
    assert custom_list.to_string() == "[]"

def test_compare(custom_list):
    """Test comparing two CustomList instances."""
    custom_list.add(1)
    custom_list.add(2)
    
    other_list = CustomList()
    other_list.add(1)
    other_list.add(2)
    
    assert custom_list.compare(other_list) is True
    
    other_list.add(3)
    assert custom_list.compare(other_list) is False
    
    different_type = [1, 2]
    with pytest.raises(TypeError):
        custom_list.compare(different_type)

def test_filter_by_type(custom_list):
    """Test filtering items by type."""
    custom_list.add(1)
    custom_list.add("two")
    custom_list.add(3.0)
    
    int_items = custom_list.filter_by_type(int)
    assert int_items.get_item_by_index(0) == 1
    
    str_items = custom_list.filter_by_type(str)
    assert str_items.get_item_by_index(0) == "two"
    
    float_items = custom_list.filter_by_type(float)
    assert float_items.get_item_by_index(0) == float(3.0)
    
    with pytest.raises(TypeError):
        custom_list.filter_by_type("list")