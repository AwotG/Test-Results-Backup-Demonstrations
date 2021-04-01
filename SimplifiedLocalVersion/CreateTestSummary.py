import json
import logging
import subprocess
from pathlib import Path
from typing import Dict


def get_commit_hash() -> str:
    cmd = ["git", "rev-parse", "--verify", "HeAD"]

    commit_hash_run = subprocess.run(cmd, capture_output=True)

    if commit_hash_run.returncode != 0:
        logging.error("Something went wrong when trying to grab the git commit.")
        logging.error(f"{commit_hash_run.stderr.decode('utf-8')}")
        return None
    else:
        return commit_hash_run.stdout.decode("utf-8").strip()


def parse_for_summary(report_path: Path) -> Dict:
    tally = dict(total=0, passed=0, skipped=0, failed=0, untested=0, broken=0)
    testcase_results = []
    git_commit_hash = get_commit_hash()

    for file in report_path.glob("*result.json"):
        results = json.load(file.open(mode="r"))
        status = results["status"]
        test_name = results["fullName"]
        testcase_results.append(dict(name=test_name, status=status))
        tally["total"] += 1
        tally[status] += 1

    final_output = dict(git_hash=git_commit_hash,summary=tally, results=testcase_results)

    return final_output


def create_summary_file(report_path: Path) -> None:
    output = report_path.parent.joinpath("summary.json")
    summary = parse_for_summary(report_path)

    with output.open(mode="w") as summary_file:
        json.dump(summary, summary_file, indent=4)

    return None


def generate_allure_report(report_path: Path) -> None:
    allure_output = report_path.parent.joinpath("allure-report")

    cmd = ["allure", "generate", str(report_path), "-o", str(allure_output)]
    results = subprocess.run(cmd, capture_output=True)

    if results.returncode != 0:
        logging.error(results.stderr.decode('utf-8'))
    else:
        logging.info(results.stdout.decode('utf-8'))
    return