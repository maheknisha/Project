from flask import Flask, request, jsonify
from flask_mysqldb import MySQL  

app= Flask(__name__)
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] ='MySql@1234' #database password
app.config['MYSQL_DB'] = 'ecommerce' #database name
mysql = MySQL(app)
#User api with post method
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    #name and email are mandatory
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        if "Duplicate entry" in str(e):
            return jsonify({'error': 'Email already exists'}), 409
        return jsonify({'error': str(e)}), 400


#User api with get method
@app.route('/user', methods=['GET'])
def list_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, email FROM users")
    users = cur.fetchall()
    cur.close()

    return jsonify([
        {'id': u[0], 'name': u[1], 'email': u[2]}
        for u in users
    ])


#products api with post method
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')
     #stock ,name, price validation
    if name is None or price is None or stock is None:
        return jsonify({'error': 'Name, price and stock are required'}), 400

    if price < 0 or stock < 0:
        return jsonify({'error': 'Invalid price or stock'}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
            (name, price, stock)
        )
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Product created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

#product api with get methods
@app.route('/products', methods=['GET'])
def list_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, price, stock FROM products")
    products = cur.fetchall()
    cur.close()

    return jsonify([
        {'id': p[0], 'name': p[1], 'price': float(p[2]), 'stock': p[3]}
        for p in products
    ])


# Orders api with post method
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    items = data.get('items')

    if not user_id or not items:
        return jsonify({'error': 'User ID and items required'}), 400

    try:
        cur = mysql.connection.cursor()

        # Check user
        cur.execute("SELECT id FROM users WHERE id=%s", (user_id,))
        if not cur.fetchone():
            return jsonify({'error': 'User not found'}), 404

        # checking of order status
        cur.execute(
            "INSERT INTO orders (user_id, status) VALUES (%s,'PENDING')",
            (user_id,)
        )
        order_id = cur.lastrowid
        # Process items
        

        for item in items:
            product_id = item['product_id']
            qty = item['quantity']
            cur.execute(
                "SELECT stock, price FROM products WHERE id=%s",
                (product_id,)
            )
            product = cur.fetchone()
            if not product:
                return jsonify({'error':f'Product{product_id}not found'}),404
            if product[0] <qty:
                return jsonify({'error':f'Insufficient stock for product{product_id}'}), 400
            price = product[1]
            cur.execute(
                """
                INSERT INTO order_items(order_id,product_id, quantity, price)
                VALUES(%s,%s,%s,%s)""",
                (order_id,product_id, qty, price)
            )
            cur.execute(
                "UPDATE products SET stock = stock - %s WHERE id=%s",
                (qty, product_id)
            )
        mysql.connection.commit()
        cur.close()
        return jsonify({
            'message':'Order created successfully',
            'order_id': order_id
        }),201
    except Exception as e:
        return jsonify({'error':str(e)}),400
@app.route('/orders',methods=['GET'])
def list_orders(): #pagination
    status = request.args.get('status')
    page = int(request.args.get('page',1))
    limit = int(request.args.get('limit',10))
    offset = (page - 1) * limit
    cur = mysql.connection.cursor()
    if status:
        cur.execute(
    "SELECT id, user_id, status, created_at FROM orders WHERE status=%s LIMIT %s OFFSET %s",
    (status, limit, offset)
)
    else:
        cur.execute(
            "SELECT id,user_id, status, created_at FROM orders LIMIT %s OFFSET %s",
            (limit, offset)
        )
    orders = cur.fetchall()
    cur.close()
    return jsonify([
        {
            'id':o[0],
            'user_id':o[1],
            'status':o[2],
            'created_at':str(o[3])

        }
        for o in orders
    ])


# running flask app
if __name__ == "__main__":
   app.run(debug=True)
   
