# 导入所需的库
from xtquant import xttrader
from xtquant.xttype import StockAccount
import random

##订阅账户
# 设置 QMT 交易端的数据路径和会话ID
min_path = r"D:\国金证券QMT交易端\userdata_mini"
session_id = int(random.randint(100000, 999999))  # 随机生成会话ID

# 创建 XtQuantTrader 实例并启动
xt_trader = xttrader.XtQuantTrader(min_path, session_id)
xt_trader.start()

# 连接 QMT 交易端
connect_result = xt_trader.connect()
if connect_result == 0:
    print('连接成功')
else:
    print('连接失败')
    xt_trader.stop()
    exit()

# 设置账户信息
account = '8884417387'
acc = StockAccount(account)

# 订阅账户
res = xt_trader.subscribe(acc)
if res == 0:
    print('订阅成功!')
else:
    print('订阅失败!')