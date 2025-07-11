class StringUtils:
    @staticmethod
    def change_case(input_string: str, to_upper: bool = True) -> str:
        return input_string.upper() if to_upper else input_string.lower()
    
    @staticmethod
    def check_palindrome(input_string: str) -> bool:
        cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
        reversed_string = cleaned_string[::-1]
        return cleaned_string == reversed_string
    
    @staticmethod
    def count_words(input_string: str) -> int:
        import re
        words = re.split(r'[ ,:;.!?"\'\n\r\t]+', input_string.strip())
        return len([word for word in words if word])
    
    @staticmethod
    def type_of_string(input_string: str) -> str:
        if input_string.isdigit():
            return "Integer"
        elif input_string.replace('.', '', 1).isdigit():
            return "Float"
        elif input_string.isalpha():
            return "Alphabetic"
        elif any(char.isdigit() for char in input_string):
            return "Alphanumeric"
        else:
            return "Unknown"
        
    @staticmethod
    def split_string(input_string: str, delimiter: str = ' ') -> list:
        if delimiter not in input_string:
            return [input_string]
        return input_string.split(delimiter)
    
    @staticmethod
    def combine_to_string(input_list: list, delimiter: str = ' ') -> str:
        return delimiter.join(input_list)
    
    @staticmethod
    def replace_substring(input_string: str, old: str, new: str) -> str:
        return input_string.replace(old, new)
    
    @staticmethod
    def is_start_with(input_string: str, prefix: str) -> bool:
        return input_string.startswith(prefix)
    
    @staticmethod
    def trim_string(input_string: str, count: int = 0) -> str:
        if count <= 0:
            raise ValueError("Count must be greater than 0")
        if count >= len(input_string):
            return input_string
        return str(input_string[:count] + "...")
    
if __name__ == "__main__":
    utils = StringUtils()
    print(utils.change_case("Hello World", to_upper=False))
    print(utils.check_palindrome("LOL"))
    print(utils.count_words("Hello, world! This is a test."))
    print(utils.type_of_string("12345"))
    print(utils.split_string("Hello, world! This is a test."))
    print(utils.combine_to_string(["Hello", "world!"], delimiter=", "))
    print(utils.replace_substring("Hello, world!", "world", "Python"))
    print(utils.is_start_with("Hello, world!", "Hello"))
    print(utils.trim_string("Hello, world!", count=5))