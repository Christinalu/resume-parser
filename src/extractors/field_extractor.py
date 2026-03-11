from abc import ABC, abstractmethod

# Abstract base class for field extractors. It defines a common interface for all extractors,
# ensuring that they implement the extract method to extract specific information from the resume text.
class FieldExtractor(ABC):
    @abstractmethod
    def extract(self, text: str) -> str:
        """Extract specific information from the resume text."""
        raise NotImplementedError("Subclasses must implement the extract method.")