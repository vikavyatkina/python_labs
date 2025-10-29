import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    p = Path(path)

    if p.exists() == False:
        raise FileNotFoundError
    
    return p.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    row_list = list(rows)

    if row_list:

        first_length = len(row_list[0])

        for i, row in enumerate(row_list):

            if len(row) != first_length:

                raise ValueError()
    ensure_parent_dir(path)

    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)

txt = read_text("data/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV

