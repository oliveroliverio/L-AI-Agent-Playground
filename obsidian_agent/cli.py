import argparse
import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from obsidian_agent.loader import VaultLoader
from obsidian_agent.search import SimpleSearcher
from obsidian_agent.distiller import Distiller

def main():
    console = Console()
    
    parser = argparse.ArgumentParser(description="Obsidian Agent - Vibe Coding Edition")
    parser.add_argument("--vault", required=True, help="Path to your Obsidian Vault")
    parser.add_argument("--query", required=True, help="What you want to ask your notes")
    parser.add_argument("--model", default="gpt-4o", help="LLM Model to use")
    
    args = parser.parse_args()
    
    # 1. Load
    with console.status("[bold green]Loading Vault...[/bold green]"):
        try:
            loader = VaultLoader(args.vault)
            notes = loader.get_all_notes()
            console.print(f"[green]✓[/green] Loaded {len(notes)} notes.")
        except Exception as e:
            console.print(f"[bold red]Error loading vault:[/bold red] {e}")
            sys.exit(1)

    # 2. Search
    with console.status(f"[bold blue]Searching for '{args.query}'...[/bold blue]"):
        searcher = SimpleSearcher()
        relevant_notes = searcher.search(notes, args.query)
        console.print(f"[blue]✓[/blue] Found {len(relevant_notes)} relevant notes.")
        
    if not relevant_notes:
        console.print("[yellow]No relevant notes found. Try a different keyword.[/yellow]")
        sys.exit(0)

    # 3. Distill
    with console.status("[bold purple]Distilling insights with LLM...[/bold purple]"):
        distiller = Distiller(model=args.model)
        result = distiller.distill(args.query, relevant_notes)

    # 4. Output
    console.print(Panel(Markdown(result), title=f"Distilled insights for: '{args.query}'", border_style="purple"))

if __name__ == "__main__":
    main()