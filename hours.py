#!/usr/bin/env python
"""Hours

A simple, single module Python application for calculating and tracking hours
using CSV file(s).

"""

import csv
from datetime import datetime, date, time, timedelta
from pathlib import Path
from typing import Any

import typer
import pandas as pd
from pydantic import BaseModel
from rich.console import Console

app = typer.Typer()


def read_csv(location: str) -> pd.DataFrame:
    """Convert a CSV or directory of CSVs to a Pandas DataFrame"""
    loc = Path(location)
    csv_files = []
    if loc.is_dir():
        csv_files = loc.glob("*.csv")
    else:
        csv_files.append(location)

    entries = pd.concat(pd.read_csv(file) for file in csv_files)
    entries.index = range(1, len(entries) + 1)

    return entries


def control_center(location: str) -> None:
    df_entries = read_csv(location)

    console = Console()
    console.print(df_entries)


def main() -> None:
    typer.run(control_center)


if __name__ == "__main__":
    main()
