#!/usr/bin/python3

from collect import get_all_data
from solve import solve_all
from freezer import freeze_all

if __name__ == "__main__":
    input_folder, output_folder = get_all_data()
    solve_all(input_folder, output_folder)
    freeze_all()
