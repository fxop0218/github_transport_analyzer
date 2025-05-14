# main.py
import typer
from rich.console import Console
from rich.table import Table
from app.github_client import GitHubClient

app = typer.Typer()
console = Console()

@app.command()
def search(
    term: str = typer.Argument(..., help="Search term or organization name"),
    language: str = typer.Option(None, "--language", "-l", help="Programming language filter"),
    sort: str = typer.Option("stars", "--sort", "-s", help="Sort by 'stars' or 'created'"), # TODO: Stars default
    limit: int = typer.Option(5, "--limit", "-n", help="Number of repositories to retrieve"),
    mode: str = typer.Option("term", "--mode", "-m", help="Search mode: 'term' or 'org'"),
):
    """
    Search GitHub repositories and display a formatted table with basic stats.
    """
    client = GitHubClient(mode=mode)
    console.print(f"[bold green]🔍 Searching for '{term}' in mode '{mode}'...[/bold green]")

    try:
        response = client.search_repositories(term, language, sort, limit)
        repos = response.get("items", [])

        table = Table(title=f"Top {len(repos)} repositories")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Stars", style="yellow")
        table.add_column("Language", style="magenta")
        table.add_column("URL", style="blue")

        for repo in repos:
            table.add_row(
                repo.get("full_name", "N/A"),
                str(repo.get("stargazers_count", 0)),
                repo.get("language", "-"),
                repo.get("html_url", "N/A")
            )

        console.print(table)

    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {e}")

if __name__ == "__main__":
    app()
