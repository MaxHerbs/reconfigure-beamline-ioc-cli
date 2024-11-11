import typer
from typing import Optional
from typing_extensions import Annotated
from reconfigure_ioc_cli.Cluster import ClusterEngine

import reconfigure_ioc_cli.Cluster


app = typer.Typer()


@app.command()
def setup(
    beamline: Annotated[Optional[str], typer.Option(..., help="The beamline to configure. eg. p99")]=None,
    repository: Annotated[Optional[str], typer.Option(..., help="The full repository url to clone.")]=None,
):
    """
    Runs a first time setup for the CLI.
    Can be used idempotently to update current files.
    """

    print(f"Running first time setup")
    raise NotImplementedError("Not implemented yet")
    

@app.command()
def restore_legacy():
    """
    Restores the legacy ioc structure
    """
    print(f"Restoring legacy ioc structure")
    raise NotImplementedError("Not implemented yet")



@app.command()    
def kube_restore(
    restore_file: Annotated[Optional[str], typer.Option(..., help="Path to a custom restore path for kubernetes restore.")]=None,
):
    """
    Restores a k8s cluster from a backup file.
    Defaults to most recent backup file stored in shared area
    """
    print(f"Restoring k8s cluster")
    raise NotImplementedError("Not implemented yet")


@app.command()
def kube_state():
    """
    Checks the state of the k8s cluster
    """
    print(f"Checking k8s cluster state")
    engine = ClusterEngine()
    raise NotImplementedError("Not implemented yet")

if __name__ == "__main__":
    app()