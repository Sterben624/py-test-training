import os
import shutil

class FileManager:
 
    @staticmethod
    def write_file(file_path, content):
        """Write content to the file."""
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def read_file(file_path):
        """Read the content of the file."""
        with open(file_path, 'r') as file:
            content = file.read()
            return content

    @staticmethod
    def append_to_file(file_path, content):
        """Append content to the file."""
        with open(file_path, 'a') as file:
            file.write(content)
    
    @staticmethod
    def is_exists(file_path):
        """Check if the file exists."""
        return os.path.exists(file_path)
        
    @staticmethod
    def create_directory(directory_path):
        """Create a directory if it does not exist."""
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        
    @staticmethod
    def delete_file(file_path):
        """Delete the specified file."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
    @staticmethod
    def delete_directory(directory_path):
        """Delete the specified directory."""
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
        else:
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")
        
    @staticmethod
    def size_of_file(file_path):
        """Get the size of the file in bytes."""
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist.")

    @staticmethod
    def size_of_directory(directory_path):
        """Get the size of the directory in bytes."""
        if os.path.exists(directory_path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size
        else:
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")
        
    @staticmethod
    def list_files_in_directory(directory_path):
        """List all files in the specified directory."""
        if os.path.exists(directory_path):
            return os.listdir(directory_path)
        else:
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")
        
    @staticmethod
    def copy_file(source_path, destination_path):
        """Copy a file from source to destination."""
        if os.path.exists(source_path):
            with open(source_path, 'rb') as src_file:
                content = src_file.read()
            with open(destination_path, 'wb') as dest_file:
                dest_file.write(content)
        else:
            raise FileNotFoundError(f"The source file {source_path} does not exist.")
        
    @staticmethod
    def move_file(source_path, destination_path):
        """Move a file from source to destination."""
        if os.path.exists(source_path):
            os.rename(source_path, destination_path)
        else:
            raise FileNotFoundError(f"The source file {source_path} does not exist.")
        
    @staticmethod
    def rename_file(file_path, new_name):
        """Rename a file."""
        if os.path.exists(file_path):
            directory = os.path.dirname(file_path)
            new_file_path = os.path.join(directory, new_name)
            os.rename(file_path, new_file_path)
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
    @staticmethod
    def search_file_like(directory_path, pattern):
        """Search for files in the directory that match the pattern."""
        if os.path.exists(directory_path):
            matching_files = []
            for dirpath, dirnames, filenames in os.walk(directory_path):
                for filename in filenames:
                    if pattern in filename:
                        matching_files.append(os.path.join(dirpath, filename))
            return matching_files
        else:
            raise FileNotFoundError(f"The directory {directory_path} does not exist.")
        
    