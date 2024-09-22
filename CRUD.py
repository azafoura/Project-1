import mysql.connector

class CRUDModel:
    # MySQL database connection
    conn = mysql.connector.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7731574",
        password="eWDTurJ4v2",
        database="sql7731574"
    )
    cursor = conn.cursor()

    def __init__(self, table_name, record_id):
        self.table_name = table_name
        self.record_id = record_id

    @classmethod
    def create(cls, table_name, **kwargs):
        """Insert a new record into the table."""
        columns = ", ".join(kwargs.keys())
        placeholders = ", ".join(['%s' for _ in kwargs])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cls.cursor.execute(sql, tuple(kwargs.values()))
        cls.conn.commit()
        print(f"New record inserted into {table_name}.")
        return cls(table_name, cls.cursor.lastrowid)

    def read(self):
        """Retrieve a single record by ID."""
        sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
        self.cursor.execute(sql, (self.record_id,))
        record = self.cursor.fetchone()
        if record:
            print(record)
            return record
        else:
            print(f"Record with ID {self.record_id} not found in {self.table_name}.")
            return None

    def update(self, **kwargs):
        """Update an existing record."""
        updates = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        sql = f"UPDATE {self.table_name} SET {updates} WHERE id = %s"
        self.cursor.execute(sql, (*kwargs.values(), self.record_id))
        self.conn.commit()
        print(f"Record with ID {self.record_id} updated in {self.table_name}.")

    @classmethod
    def delete(cls, table_name, record_id):
        """Delete a record from the table."""
        sql = f"DELETE FROM {table_name} WHERE id = %s"
        cls.cursor.execute(sql, (record_id,))
        cls.conn.commit()
        print(f"Record with ID {record_id} deleted from {table_name}.")

    @classmethod
    def get_by_id(cls, table_name, record_id):
        """Fetch a record by ID."""
        sql = f"SELECT * FROM {table_name} WHERE id = %s"
        cls.cursor.execute(sql, (record_id,))
        record = cls.cursor.fetchone()
        return record

    @classmethod
    def get_all(cls, table_name):
        """Fetch all records from the table."""
        sql = f"SELECT * FROM {table_name}"
        cls.cursor.execute(sql)
        records = cls.cursor.fetchall()
        return records


# Product subclass
class Product(CRUDModel):
    table_name = "products"

    def __init__(self, product_id, name, category, stock_level, price, low_stock_threshold, supplier_id):
        super().__init__(Product.table_name, product_id)
        self.name = name
        self.category = category
        self.stock_level = stock_level
        self.price = price
        self.low_stock_threshold = low_stock_threshold
        self.supplier_id = supplier_id


# Sale subclass
class Sale(CRUDModel):
    table_name = "sales"

    def __init__(self, sale_id, product_id, quantity_sold, price_per_unit, total_sale_value, transaction_id):
        super().__init__(Sale.table_name, sale_id)
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.price_per_unit = price_per_unit
        self.total_sale_value = total_sale_value
        self.transaction_id = transaction_id


# Employee subclass
class Employee(CRUDModel):
    table_name = "employees"

    def __init__(self, employee_id, name, role, hire_date):
        super().__init__(Employee.table_name, employee_id)
        self.name = name
        self.role = role
        self.hire_date = hire_date


# Supplier subclass
class Supplier(CRUDModel):
    table_name = "suppliers"

    def __init__(self, supplier_id, name):
        super().__init__(Supplier.table_name, supplier_id)
        self.name = name
