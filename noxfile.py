import nox


@nox.session()
def lint(session):
    session.install("flake8", "black")
    session.run("black", "--line-length=120", "--diff", "src")
    session.run("flake8", "src")


@nox.session()
def format(session):
    session.install("black")
    session.run("black","--line-length=120", "src")


@nox.session()
def test(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "src")