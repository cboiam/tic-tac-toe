# Tic tac toe

This is a classic tic-tac-toe game that runs on websocket to enable instant communication between the players.

I used this project to practice the development of a rich domain with tdd out of the context that i'm used to and also try new technologies such as flask and websocket.

## Running the application

Install the requirements listed in `src/webserver/requirements.txt`

Run the following command in the top level folder to start the webserver:

```
$ python -m src.webserver.app
```

To start the frontend go to `src/webapp` and use the command:

```
$ npm start
```

Then access http://localhost:3000/ to see the app running.

## Running the tests

Run the following command in the top level folder:

```
$ python -m unittest discover -s ./src/tests -p *Test.py
```

## Built with

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [Unittest](https://docs.python.org/3/library/unittest.html)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
- [Socket.io](https://socket.io/)
- [React](https://reactjs.org/)
