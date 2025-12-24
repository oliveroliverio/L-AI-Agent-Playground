import os
from typing import List, Dict
import openai 

class Distiller:
    def __init__(self, api_key: str = None, model: str = "gpt-4o"):
        # Vibe-Coding: Environment Variables
        # We look for the key in the environment first. Easier than hardcoding!
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        
        if not self.api_key:
            print("Warning: No API Key provided. Distiller will not work.")
            self.client = None
        else:
            self.client = openai.OpenAI(api_key=self.api_key)

    def distill(self, query: str, notes: List[Dict[str, str]]) -> str:
        """
        Summarizes the key points from the provided notes relative to the query.
        """
        if not notes:
            return "No notes found to distill."
        
        if not self.client:
            return "Error: No API client initialized (missing key?)."
        
        # Vibe-Coding: Context Stuffing
        # We take the content of the files and "stuff" them into the prompt.
        # CAUTION: Note len(note['content']). If you have huge notes, 
        # we might need to truncate them or use a smarter method later.
        context_text = ""
        for note in notes:
            context_text += f"--- FILE: {note['filename']} ---\n"
            # Truncating to 3000 chars per file for safety in this v0
            context_text += note['content'][:3000] 
            context_text += "\n\n"
        
        prompt = f"""
        You are a research assistant. 
        User Query: "{query}"
        
        Here are some relevant notes from the user's Obsidian vault:
        
        {context_text}
        
        Based ONLY on these notes, provide a concise summary or answer to the query.
        Start with "Here is what I found in your notes:"
        """
        
        try:
            print("DEBUG: Sending request to LLM...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error distilling notes: {e}"