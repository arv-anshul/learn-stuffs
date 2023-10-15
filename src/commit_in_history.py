import subprocess
from datetime import datetime as dt
from datetime import timedelta

commit_message = "⏰ Commit in Past!"
commit_time = dt.now() - timedelta(days=76)

git_command = [
    "git",
    "commit",
    "--date",
    str(commit_time),
    "-m",
    commit_message,
]

_git_command = [
    "git",
    "commit",
    "--amend",
    "--no-edit",
    # "-m", commit_message,
    "--date",
    f"{commit_time}",
]

if __name__ == "__main__":
    # print(commit_time)
    subprocess.call(git_command)
