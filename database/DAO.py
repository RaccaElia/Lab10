from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getSituaBeforeYear(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select state1no, state2no
                    from contiguity
                    where conttype = 1 AND year <= %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append([row["state1no"], row["state2no"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from country"""

        cursor.execute(query)

        for row in cursor:
            result.append(Stato(row["StateNme"], row["StateAbb"], row["CCode"]))

        cursor.close()
        conn.close()
        return result
