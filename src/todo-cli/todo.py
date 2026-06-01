#! usr/bin/env python3

import typer


def main(age: str):
    print(f"hello {age}")


if __name__ == "__main__":
    typer.run(main)
