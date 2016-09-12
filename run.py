from flask import Flask, request, redirect, session
import twilio.twiml

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+15106935609": "Sophia Liu",
    "+19165090941": "Bry Bach",
    "+17609201596": "Madison Pauly",
    "+17073865096": "Dayna Tran",
    "+15102834827": "Jo Jin Leong",
    "+15104565229": "Surina Gulati",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond with the number of text messages sent between two parties."""

    counter = session.get('counter', 0)

    # increment the counter
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Student"

    message = "".join([name, " has messaged ", request.values.get('To'), " ",
        str(counter), " times."])
    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
