from abc import ABC, abstractmethod

# Abstract base class for resume parsers. It defines a common interface for all parsers, 
# ensuring that they implement the parse method to extract resume content from a given file path.
class FileParser(ABC):
    @abstractmethod
    # The parse method is an abstract method that must be implemented by any subclass of FileParser.
    def parse(self, file_path: str) -> str:
        """Parse the resume file and return its content as a string."""
        raise NotImplementedError("Subclasses must implement the parse method.")