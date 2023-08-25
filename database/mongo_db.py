import pymongo


class MongoDb:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    def __init__(self, client_name, col_name):
        self.mydb = MongoDb.myclient[client_name]
        self.mycol = self.mydb[col_name]
        self.username_id = self.mydb['username_id']

    # 自增函数
    def getNextValue(self, user_Name):
        ret = self.username_id.find_one_and_update({"_id": user_Name}, {"$inc": {"sequence_value": 1}})

        new = ret["sequence_value"]
        return new

    def auto_id_genertator(self):
        # 创建username_id集合,初始id为0
        self.username_id.insert_one(({'_id': "name", 'sequence_value': 0}))
