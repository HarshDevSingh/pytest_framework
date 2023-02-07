import argparse
import os
import subprocess


def _test_command_builder(verbose=True, test_file_loc: str = ""):
    s = ""
    if verbose:
        s = "-s"
    cmd = f"pytest {s} {test_file_loc}"
    return cmd


def run_tests():
    cmd = _test_command_builder()
    response = subprocess.run(str(cmd), shell=True)
    assert response.returncode == 0, "pytest execution failed"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", required=True, \
                        help="chrome, firefox browsers are expected")
    args = parser.parse_args()
    os.environ["BROWSER"] = args.browser.lower()
    if not os.environ["BROWSER"] or os.environ["BROWSER"] not in ["chrome", "firefox"]:
        raise ValueError("browser name was either empty or invalid browser was provided")
    run_tests()
