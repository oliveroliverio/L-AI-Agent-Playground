import os
from typing import List, Dict, Generator

class VaultLoader:
    def __init__(self, vault_path: str):
        self.vault_path = os.path.abspath(vault_path)
        if not os.path.exists(self.vault_path):
            raise FileNotFoundError(f"The vault path at {self.vault_path} does not exist.")

    def load_files(self) -> Generator[Dict[str, str], None, None]:
        """
        Recursively walks the vault path and yields markdown files.
        Returns a dictionary with 'path', 'filename', and 'content'.
        """
        # DEBUG: Helpful to see where it's looking if things go wrong
        print(f"DEBUG: Walking through {self.vault_path}")
        
        for root, _, files in os.walk(self.vault_path):
            for file in files:
                if file.lower().endswith(".md"):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        yield {
                            "path": full_path,
                            "filename": file,
                            "content": content
                        }
                    except Exception as e:
                        print(f"Error reading {full_path}: {e}")

    def get_all_notes(self) -> List[Dict[str, str]]:
        """
        Helper method to return all notes as a list instead of generator.
        Useful if the vault is small, but careful with memory on huge vaults!
        """
        return list(self.load_files())