from typing import List, Dict

class SimpleSearcher:
    def __init__(self):
        pass

    def search(self, notes: List[Dict[str, str]], query: str) -> List[Dict[str, str]]:
        """
        Filters notes based on whether the query string appears in the content.
        Case-insensitive.
        """
        query_lower = query.lower()
        results = []
        
        # Vibe-Coding Concept: Filtering
        # We are simply iterating through every note and checking if the string exists.
        # Simple, but effective for small-to-medium vaults.
        for note in notes:
            if query_lower in note['content'].lower():
                results.append(note)
        
        return results