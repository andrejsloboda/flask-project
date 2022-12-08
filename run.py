from mdblog.cli import flask_app
from mdblog.cli import init_db

import sys

def start():
    debug = False
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)


def init():   
    init_db(flask_app)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "start":
            start()
        elif command == "init":
            init()
    else:
        print("usage:\n\n\trun.py [ start | init ]")
