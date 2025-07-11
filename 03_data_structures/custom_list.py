class CustomList:
    def __init__(self):
        self.items = []

    def add(self, item):
        """Add an item to the list."""
        self.items.append(item)

    def add_index(self, item, index):
        """Add an item to the list at a specific index."""
        if 0 <= index <= len(self.items):
            self.items.insert(index, item)
        else:
            raise IndexError("Index out of range")

    def remove(self, item=None, index=None):
        """Remove an item from the list by value or index."""
        if index is not None:
            if 0 <= index < len(self.items):
                del self.items[index]
            else:
                raise IndexError("Index out of range")
        else:
            try:
                self.items.remove(item)
            except ValueError:
                raise ValueError("Item not found in the list")

    def get_copy_list(self):
        """Return a copy of the items in the list."""
        return self.items.copy()
    
    def get_item_by_index(self, index):
        """Return the item at a specific index."""
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("Index out of range")
        
    def get_length(self):
        """Return the number of items in the list."""
        return len(self.items)
    
    def is_empty(self):
        """Check if the list is empty."""
        return len(self.items) == 0
    
    def clear(self):
        """Clear all items from the list."""
        self.items.clear()

    def search_index_item(self, item):
        """Search for an item and return its index, or -1 if not found."""
        try:
            return self.items.index(item)
        except ValueError:
            return -1
        
    def is_has_item(self, item):
        """Check if an item exists in the list."""
        return item in self.items
    
    def count_item(self, item):
        """Count how many times an item appears in the list."""
        return self.items.count(item)
    
    def reverse(self):
        """Reverse the order of items in the list."""
        self.items.reverse()

    def sort(self, reverse=False):
        """Sort the items in the list."""
        self.items.sort(reverse=reverse)

    def get_sublist_in_range(self, start, end):
        """Return a sublist from start to end index."""
        if start < 0 or end < 0:
            raise IndexError("Start and end indices must be non-negative")
        if start >= end:
            raise IndexError("Start index must be less than end index")
        if 0 <= start < len(self.items) and 0 <= end <= len(self.items):
            return self.items[start:end]
        else:
            raise IndexError("Index out of range")
        
    def merge(self, other_list):
        """Merge another CustomList into this one."""
        if isinstance(other_list, CustomList):
            self.items.extend(other_list.items)
        else:
            raise TypeError("Argument must be an instance of CustomList")
        
    def to_string(self):
        """Return a string representation of the list."""
        return str(self.items)
    
    def compare(self, other_list):
        """Compare this list with another CustomList."""
        if isinstance(other_list, CustomList):
            return self.items == other_list.items
        else:
            raise TypeError("Argument must be an instance of CustomList")
        
    def filter_by_type(self, item_type):
        """Filter items by type and return a new CustomList."""
        if not isinstance(item_type, type):
            raise TypeError("item_type must be a type")
        filtered_items = [item for item in self.items if isinstance(item, item_type)]
        new_list = CustomList()
        new_list.items = filtered_items
        return new_list