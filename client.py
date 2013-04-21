import cameratasks

from flask import Flask
app = Flask(__name__)


@app.route("/shoot")
def shoot():
    cameratasks.click(12)
    return "shot!"


@app.route("/cleanup")
def cleanup():
    cameratasks.cleanup()
    return "cleaned up gpio"

if __name__ == "__main__":
    app.run()
