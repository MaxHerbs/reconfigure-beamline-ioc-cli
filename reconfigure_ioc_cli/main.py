import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def setup(
    beamline: Annotated[str, typer.Argument(..., help="The beamline to configure."),]
):
    """
    Runs a first time setup for the CLI.
    Can be used idempotently to update current files.
    """

    print(f"Running first time setup")
    raise NotImplementedError("Not implemented yet")
     
@app.command()
def version():
    """
    Prints the version of the CLI.
    """
    print("0.1.0")  
    typer.Exit(0)


if __name__ == "__main__":
    app()