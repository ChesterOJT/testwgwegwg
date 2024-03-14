from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_voltage')
def get_voltage():
    # Open serial port
    ser = serial.Serial('COM5', 9600)  # Change to your Arduino port
    try:
        # Read data from Arduino
        data = ser.readline().decode().strip()
        # Extract voltage value
        voltage_str = data.split(": ")[1]
        voltage = float(voltage_str)
        return jsonify(voltage=voltage)
    finally:
        # Close serial port
        ser.close()

