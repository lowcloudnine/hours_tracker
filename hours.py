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
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

app = typer.Typer()


class HourEntry(BaseModel):
    """Class for tracking an entry of hours."""

    year: int
    month: int
    day: int
    start: time
    stop: time
    note: str = ""


def read_csv(file_name: str | Path) -> list[dict[str, Any]]:
    """Read a CSV file at file_name and return a list of the rows."""
    entries = []
    with open(file_name, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row = {key.strip(): value.strip() for key, value in row.items()}
            entries.append(HourEntry(**row))

    return entries


def control_center(input_file: str) -> None:
    console = Console()
    console.print(read_csv(file_name=input_file))


def main() -> None:
    typer.run(control_center)


if __name__ == "__main__":
    main()
