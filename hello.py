
@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='user',
            password='password',
            database='sampledb'
        )
        return "Connected to MySQL from Flask!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
