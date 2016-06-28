from flask import Flask, request, jsonify
from Continuation import Continuation
from StagingArea import StagingArea

app = Flask(__name__)


@app.route("/", methods=["POST"])
def create_table():
    details = request.get_json()
    table_name = staging_area.create_table(details["cols"])
    if "continuations" in details:
        for con in details["continuations"]:
            continuation.register(table_name, con)
    return jsonify({"status": "Success", "table_name": table_name, "schema": staging_area.schema})


@app.route("/continuation", methods=["POST"])
def add_continuation():
    details = request.get_json()
    table_name = details["table_name"]
    for con in details["continuations"]:
        print(con)
        continuation.register(table_name, con)
    return jsonify({"status": "Success"})


@app.route("/trigger/<table>", methods=["POST"])
def trigger_table(table):
    result = continuation.trigger(table)
    if result:
        return jsonify({"Status": "Success"})
    else:
        return jsonify({"Status": "Failure"})


if __name__ == "__main__":
    staging_area = StagingArea()
    continuation = Continuation()
    app.run(debug=True)
