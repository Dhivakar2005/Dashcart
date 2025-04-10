import sqlite3

class ProductMatchingAgent:
    """
    Matches products based on the customer's interests.
    If interests == ["General"], returns top 5 rated products.
    """
    def __init__(self, db_path):
        self.db_path = db_path

    def match_products(self, interests):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if interests == ["General"]:
            query = """
                SELECT ProductID, SubCategory, Category, Price, ProductRating
                FROM products
                ORDER BY ProductRating DESC
                LIMIT 5
            """
            cursor.execute(query)
        else:
            conditions = []
            params = []
            for interest in interests:
                conditions.append("(SubCategory LIKE ? OR Category LIKE ?)")
                params.extend([f"%{interest}%", f"%{interest}%"])
            where_clause = " OR ".join(conditions)
            query = f"""
                SELECT ProductID, SubCategory, Category, Price, ProductRating
                FROM products
                WHERE {where_clause}
                ORDER BY ProductRating DESC
                LIMIT 5
            """
            cursor.execute(query, params)

        rows = cursor.fetchall()
        conn.close()

        product_list = []
        for r in rows:
            product_list.append({
                "product_id": r[0],
                "product_name": r[1],
                "category": r[2],
                "price": r[3],
                "rating": r[4]
            })
        return product_list
