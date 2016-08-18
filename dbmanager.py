
from pymongo import MongoClient

class DBManager:
    def __init__(self):
        print("DBManager init")
    def get_db(self):
        client = MongoClient('localhost:27017')
        db = client.tensorDB
        return db
    def data_insert(self,path,re,sc):
        db = self.get_db()
        db.tensorDB.insert({"ImagePath" : path,
        "result_1" : re[0],"result_2" : re[1],"result_3" : re[2],
        "result_4" : re[3],"result_5" : re[4],
        "result_1_rate" : str(sc[0]),"result_2_rate" : str(sc[1]),
        "result_3_rate" : str(sc[2]),"result_4_rate" : str(sc[3]),
        "result_5_rate" : str(sc[4])})



"""
        db.tensorDB.insert({"ImagePath" : path})
        for i in range(len(re)):
            db.tensorDB.update({"ImagePath" : path},
                                "result" : re[i] , 
				"match_percentage" : sc[i]})
"""
