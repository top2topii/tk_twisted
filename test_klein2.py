from klein import Klein
app = Klein()

@app.route('/')
def pg_root(request):
    return 'I am the root2 page!'

@app.route('/about2')
def pg_about(request):
    return 'I am a Klein application2!'

app.run("localhost", 8089)