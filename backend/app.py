from app_factory import create_app

app = create_app(config_name="DEVELOPMENT")
app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5120)
