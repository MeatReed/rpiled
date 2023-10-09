from app import app
import argparse

if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()