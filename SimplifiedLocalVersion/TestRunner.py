import logging
import subprocess
from datetime import datetime
from pathlib import Path

from CreateTestSummary import create_summary_file, generate_allure_report
from ErrorHandling import PytestExitCodes, BehaveExitCodes
from FileOrganization import FOLDER_ROOT, create_latest_ran_folder, create_past_runs_directory,\
    move_last_run_reports_to_past

LAST_RUN_FOLDER = create_latest_ran_folder()
PAST_RUN_FOLDER = create_past_runs_directory()


def run_pytest_suite() -> None:
    test_suite = FOLDER_ROOT.joinpath("SimulatedTestSuites", "allure-python", "allure-python-pytest", "test")

    timestamp = int(datetime.now().timestamp())
    results_name = f"pytest_{timestamp}"
    output_directory = LAST_RUN_FOLDER.joinpath(results_name)

    unprocessed_results_output = output_directory.joinpath("unprocessed-results")

    run_cmd = ["pytest", f"--alluredir={unprocessed_results_output}", test_suite]
    results = subprocess.run(run_cmd, capture_output=True)

    failure_codes = [PytestExitCodes.INTERNAL_ERROR.value, PytestExitCodes.CMDLINE_ERROR.value, PytestExitCodes.NO_TESTS_COLLECTED.value]

    if results.returncode in failure_codes:
        raise Exception(f"{results.stderr.decode('utf-8')}")
    else:
        logging.info(f"{results.stdout.decode('utf-8')}")
        generate_allure_report(unprocessed_results_output)
        create_summary_file(unprocessed_results_output)
    return unprocessed_results_output


def run_behave_suite() -> None:
    test_suite = FOLDER_ROOT.joinpath("SimulatedTestSuites", "allure-python", "allure-python-behave", "features")

    timestamp = int(datetime.now().timestamp())
    results_name = f"behave_{timestamp}"
    output_directory = LAST_RUN_FOLDER.joinpath(results_name)
    unprocessed_results_output = output_directory.joinpath("unprocessed-results")

    run_cmd = ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", unprocessed_results_output, test_suite]

    results = subprocess.run(run_cmd, capture_output=True)

    failure_codes = [BehaveExitCodes.INTERNAL_ERROR.value, BehaveExitCodes.CMDLINE_ERROR.value, BehaveExitCodes.NO_TESTS_COLLECTED.value]

    if results.returncode in failure_codes:
        raise Exception(f"{results.stderr.decode('utf-8')}")
    else:
        logging.info(f"{results.stdout.decode('utf-8')}")
        generate_allure_report(unprocessed_results_output)
        create_summary_file(unprocessed_results_output)

    return unprocessed_results_output


def serve_combined_allure_report(*unprocessed_path: Path):
    cmd = ["allure", "serve"]
    for path in unprocessed_path:
        cmd.append(str(path))
    result = subprocess.run(cmd)
    return


move_last_run_reports_to_past(LAST_RUN_FOLDER, PAST_RUN_FOLDER)
unprocessed_pytest = run_pytest_suite()
unprocessed_behave = run_behave_suite()
serve_combined_allure_report(unprocessed_behave, unprocessed_pytest)

