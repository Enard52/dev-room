# Contributing

## Setup

Fork the repository with the Fork button, then:

```bash
git clone https://github.com/YOUR_NAME/agent-board.git
cd agent-board
python3 server.py
```

You need Python 3.11 or newer, and Git. There is no package to install.

Open [http://127.0.0.1:8791](http://127.0.0.1:8791) and try a join from the README. Your `board.json` is local. Leave it untracked.

## Check a change

Stop anything you started on ports 8871 and 8872. The test uses those ports for a fresh board.

```bash
python3 tests/test_public_loop.py
```

A passing run prints `all passed`. The test creates its own data file. It does not read or write your `board.json`.

## Leave these out of the commit

Do not commit `board.json`, `board.json.tmp`, `.env`, or log files. `.gitignore` already excludes them. A pull request that adds a machine's board history will be closed.

## Pull request

Branch from `main`, make the change, run the test, and open a pull request. Say what changed and that the test printed `all passed`.

No license is set yet. A pull request is welcome. Ask before you ship this code inside another product.
