from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from config import get_db_connection

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages

# Home Page
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# Blood Availability Page
@app.route('/blood_availability')
def blood_availability():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Query to fetch blood availability (count donors per blood group)
        cursor.execute("""
            SELECT blood_group, COUNT(*) AS quantity 
            FROM donors_table 
            GROUP BY blood_group
        """)

        blood_data = cursor.fetchall()  # Fetch all rows

        cursor.close()
        conn.close()

        return render_template('blood_availability.html', blood_data=blood_data)

    except mysql.connector.Error as err:
        flash(f"Database Error: {err}", "danger")
        return render_template('blood_availability.html', blood_data=[])



# Donor Registration Page
@app.route('/donor_registration', methods=['GET', 'POST'])
def donor_registration():
    if request.method == 'POST':
        name = request.form['donarName']  # Fixed form field name
        email = request.form['email']
        phone = request.form['phone']
        blood_group = request.form['bloodGroup']
        state = request.form['state']
        city = request.form['city']
        postal_code = request.form['postalCode']
        address = request.form['address']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donors_table (name, email, phone, blood_group, state, city, postal_code, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, email, phone, blood_group, state, city, postal_code, address))
            
            cursor.execute("""
                INSERT INTO donors_list (name, blood_group, phone)
                VALUES (%s, %s, %s)
            """, (name, blood_group, phone))
            conn.commit()
            flash("Donor registration successful!", "success")
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")
        finally:
            cursor.close()
            conn.close()

        return redirect('/donor_registration')  # Redirect back to form with success message

    return render_template('donor_registration.html')


# Blood Request Page
# Route for Request Blood Page (GET & POST)
@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        blood_group = request.form['bloodGroup']
        state = request.form['state']
        city = request.form['city']
        postal_code = request.form['postalCode']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into database
        cursor.execute("""
            INSERT INTO blood_requests (name, phone, email, blood_group, state, city, postal_code)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, phone, email, blood_group, state, city, postal_code))

        conn.commit()
        conn.close()

        flash("Blood request submitted successfully!", "success")
        return redirect('/request_blood')

    return render_template('request_blood.html')

# Donors List Page (Fetch data from MySQL)
@app.route('/donors_list')
def donors_list():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT name, blood_group, phone FROM donors_list")  
    donors = cursor.fetchall()  
    
    conn.close()
    
    return render_template('donors_list.html', donors=donors)

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
