# tasks.py
from invoke import task


@task
def install(c):
    """Install dependencies from requirements.txt."""
    print("Compile requirements.txt...")
    c.run("uv pip compile pyproject.toml -o requirements.txt")
    print("Installing dependencies...")
    c.run("uv pip install -r requirements.txt")
    print("Installation complete!")


@task
def pw_install(c):
    """Install all browsers required by Playwright."""
    print("Installing required browsers for Playwright...")
    c.run("playwright install")
    print("Installation complete!")
