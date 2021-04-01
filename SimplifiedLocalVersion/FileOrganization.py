import shutil
from pathlib import Path


FOLDER_ROOT = Path().absolute()


def create_all_reports_directory() -> Path:
    output_folder = FOLDER_ROOT.joinpath("all-reports")
    if not output_folder.exists():
        output_folder.mkdir()

    return output_folder


def create_past_runs_directory() -> Path:
    output_folder = create_all_reports_directory().joinpath("past-runs")
    if not output_folder.exists():
        output_folder.mkdir()

    return output_folder


def create_latest_ran_folder() -> Path:
    output_folder = create_all_reports_directory().joinpath("last-run")
    if not output_folder.exists():
        output_folder.mkdir()

    return output_folder

def move_last_run_reports_to_past(last_run_path: Path, past_run_path: Path) -> None:
    folder_items = last_run_path.glob("*")

    if bool(list(folder_items)):
        for item in last_run_path.glob("*"):
            shutil.copytree(item, past_run_path.joinpath(item.name))
            shutil.rmtree(item)
    return