#!/usr/bin/python3 -i

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello"


@app.route('/open/<video_file_name>')
def open_video_file(video_file_name):
    check_output("vlc", shell=True)
    return "I opened " + video_file_name + ". You should be proud."


@app.route('/guide/<showname>')
def episode_guide_page(showname):
    show = Episode_Guide(showname)
    random_episode = show.random_episode()
    return render_template("episode_info.html", template_folder="templates", title=random_episode[0], descr=random_episode[1],
                           season=random_episode[2], episode=random_episode[3], airdate=random_episode[4])


@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
