from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def get_anagrammi_corretti():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM parola"

        cursor.execute(query)
        for row in cursor:
            result.append(row["nome"])

        cursor.close()
        conn.close()
        return result