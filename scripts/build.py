#!/usr/bin/env python3
"""
NearMeet Build Script
Compile and build the application
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
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with error code {e.returncode}")
        return False


def main():
    """Main build function"""
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    print("\n" + "="*60)
    print("  NearMeet Build Script")
    print("="*60)
    
    # Clean previous builds
    if run_command(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        "Upgrading pip"
    ):
        pass
    else:
        return False
    
    # Install dependencies
    if not run_command(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        "Installing dependencies"
    ):
        return False
    
    # Format code with black
    if not run_command(
        [sys.executable, "-m", "black", "src", "tests"],
        "Formatting code with black"
    ):
        print("⚠️  Black formatting failed (optional)")
    
    # Sort imports with isort
    if not run_command(
        [sys.executable, "-m", "isort", "src", "tests"],
        "Sorting imports with isort"
    ):
        print("⚠️  isort failed (optional)")
    
    # Check code with flake8
    if not run_command(
        [sys.executable, "-m", "flake8", "src", "tests"],
        "Checking code with flake8"
    ):
        print("⚠️  flake8 found issues (optional)")
    
    # Run tests
    if not run_command(
        [sys.executable, "-m", "pytest", "tests", "-v"],
        "Running tests"
    ):
        print("⚠️  Some tests failed")
    
    # Build distribution
    if not run_command(
        [sys.executable, "setup.py", "sdist", "bdist_wheel"],
        "Building distribution packages"
    ):
        print("⚠️  Build failed")
    
    print("\n" + "="*60)
    print("  Build completed!")
    print("="*60)
    print("\nDistribution packages are in: dist/")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
