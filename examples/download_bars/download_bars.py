from pathlib import Path
import datetime as dt

import polars as pl

from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.database import get_database
from vnpy.trader.constant import Interval
from vnpy_tqsdk.tqsdk_datafeed import TqsdkDatafeed


datafeed: TqsdkDatafeed = get_datafeed()
database = get_database()
cur_path = Path(__file__).parent

interval = Interval.MINUTE
# df = datafeed.query_free_all(ind_class="CONT", interval=interval, data_length=1e4)
# datafeed.save_df(df=df, file_path=cur_path / f"cont_{interval.value}_df.parquet")

# df = pl.read_parquet(cur_path / f"cont_{interval.value}_df.parquet")
# early_df = datafeed.get_early_pro_data(
#     cur_df=df, interval=interval, start_datetime=dt.datetime(2016, 1, 1)
# )
# df = pl.concat([early_df, df]).sort(["jj_code", "open_time"])
# datafeed.save_df(
#     df=df, file_path=cur_path / f"cont_2010_now_{interval.value}_df.parquet"
# )

df = pl.read_parquet(cur_path / f"cont_2010_now_{interval.value}_df.parquet")

database.save_df_to_table(
    df, table_name=f'tqsdk_cont_{interval.value}_kline', bar_table_type='tqsdk'
)
