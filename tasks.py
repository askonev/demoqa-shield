from invoke import task


@task
def list(c):
    c.run("invoke --list")


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


@task
def benchmark(c):
    print("headed start")
    c.run('/usr/bin/time -f "%e" pytest ./tests/functional/test_elements.py > /dev/null')


@task
def benchmark_headless(c):
    print("headless start")
    c.run(
        '/usr/bin/time -f "%e" pytest -c pytest.headless.ini ./tests/functional/test_elements.py > /dev/null'
    )


@task
def coverage(c):
    print("Running tests with coverage...")
    c.run("coverage run -m pytest")


@task(coverage)
def coverage_report(c):
    print("coverage running")
    c.run("coverage html")
