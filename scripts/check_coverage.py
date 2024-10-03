import os
import subprocess

def install_coverage():
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "coverage"])

def run_tests_with_coverage():
    subprocess.check_call(["coverage", "run", "-m", "unittest", "discover"])

def generate_coverage_report():
    subprocess.check_call(["coverage", "report"])
    subprocess.check_call(["coverage", "html"])

def open_coverage_report():
    if os.name == 'posix':
        subprocess.check_call(["open", "htmlcov/index.html"])
    elif os.name == 'nt':
        os.startfile("htmlcov/index.html")

if __name__ == "__main__":
    install_coverage()
    run_tests_with_coverage()
    generate_coverage_report()
    open_coverage_report()