
# Add __init__.py
Added `__init__.py` to tell python this folder is a package

# Add loader.py
- Recursively walks the vault path and yields markdown files.
- Returns a dictionary with 'path', 'filename', and 'content'.

- Generators: Notice yield? This makes it a "generator". It means it reads files one-by-one rather than loading 10,000 files into RAM at once. Why might this be important for a large Obsidian vault?
Encoding: We force utf-8. Windows sometimes likes cp1252 by default—forcing UTF-8 saves us headaches later.
