from pathlib import Path
import datetime as dt

from loguru import logger
import polars as pl
from tqdm import tqdm

from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.database import get_database, DB_TZ
from vnpy.trader.constant import Interval
from vnpy.trader.utility import extract_vt_symbol
from vnpy.trader.setting import SETTINGS
from vnpy_tqsdk.tqsdk_datafeed import TqsdkDatafeed


datafeed: TqsdkDatafeed = get_datafeed()
database = get_database()
cur_path = Path(__file__).parent

interval = Interval.HOUR
# df = datafeed.query_free_all(ind_class="CONT", interval=interval, data_length=1e4)
# datafeed.save_df(df=df, file_path=cur_path / "cont_df.parquet")
df = pl.read_parquet(cur_path / "cont_df.parquet")
df = datafeed.format_df(df)
early_df = datafeed.get_early_pro_data(
    cur_df=df, interval=interval, start_datetime=dt.datetime(2010, 1, 1)
)
df = pl.concat([early_df, df]).sort(["jj_code", "open_time"])
datafeed.save_df(df=df, file_path=cur_path / "cont_2010_now_df.parquet")
