#!/usr/bin/env python3
"""
NearMeet Test Script
Run all tests and generate coverage reports
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a shell command"""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print(f"{'='*60}")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        return False


def main():
    """Main test function"""
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print("\n" + "="*60)
    print("  NearMeet Test Suite")
    print("="*60)
    
    # Run all tests with coverage
    if not run_command(
        [
            sys.executable, "-m", "pytest",
            "tests",
            "-v",
            "--cov=src",
            "--cov-report=html",
            "--cov-report=term-missing"
        ],
        "Running tests with coverage"
    ):
        return False
    
    print("\n" + "="*60)
    print("  Tests completed!")
    print("="*60)
    print("\nCoverage report: htmlcov/index.html")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
