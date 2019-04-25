from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/')
@app.route("/hello")
def hello_world():
    return ('Hello World!!!!!!!', 200)


@app.route(('/test/<search_query>'))
def search(search_query):
    return (search_query, 200)


@app.route('/integer/<int:num>')
def add_one(num):
    print(num + 1)
    return ("True", 200)


@app.route(("/float/<float:fnum>"))
def add_one_float(fnum):
    print(fnum + 1)
    return ("True", 200)


@app.route("/path/<path:folder_path>")
def folder_path_display(folder_path):
    print(folder_path)
    return ("True", 200)


if __name__ == '__main__':
    app.run()
