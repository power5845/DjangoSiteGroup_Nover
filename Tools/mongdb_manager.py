from motor import motor_asyncio
from DjangoSiteGroup_Nover import settings
# 连接monogoDB数据库
class MongoBDManager(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.mongoDB_config = settings.NOVER_MONGO_DB
        self.db = self.init_db()
        # self.collection = self.get_collection(table_name)
# 初始化mongoDB数据库
    def init_db(self):
        client = motor_asyncio.AsyncIOMotorClient(self.mongoDB_config["HOST"],self.mongoDB_config["PORT"])
        db = client[self.mongoDB_config["NAME"]]
        return db[self.mongoDB_config["TABLE"]]

    def get_collection(self,table_name):
        collection = self.db[table_name]
        return collection
# mongoDB随机获取指定数量数据 （sample随机）
    async def get_data(self,size):
        datas = await self.db.aggregate([{"$sample":{"size":size}}]).to_list(size)
        return datas

# 获取指定指定字段全部数据，返回一个列表
    async def get_data_by_feild_limit(self,field):
        cursor = self.db.find({})
        datas = [doc[field] async for doc in cursor]
        return  datas

# mongoDB测试方法
    async def findone(self):
        response_data = await self.db.find_one()
        print("mongodb :",response_data)
        return response_data
