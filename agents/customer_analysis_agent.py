import sqlite3
import ast

class CustomerAnalysisAgent:
    """
    Reads the customer's browsing history from SQLite.
    Falls back to default interests if none found.
    """
    def __init__(self, db_path):
        self.db_path = db_path
        self.fallbacks = {
            "C1000": ["Books", "Fashion"],
            "C2000": ["Electronics", "Gadgets"],
            "C3000": ["Home Decor", "Furniture"]
        }

    def analyze_customer(self, customer_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT BrowsingHistory FROM customers WHERE CustomerID=?", (customer_id,))
        row = cursor.fetchone()
        conn.close()
        if row and row[0]:
            raw_str = row[0]
            try:
                interests = ast.literal_eval(raw_str)
                if isinstance(interests, list):
                    return [str(x).strip() for x in interests]
                else:
                    return [item.strip() for item in raw_str.split(',')]
            except:
                return [item.strip() for item in raw_str.split(',')]
        else:
            return self.fallbacks.get(customer_id, ["General"])
