from pathlib import Path

import polars as pl

from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.database import get_database, DB_TZ
from vnpy.trader.constant import Interval
from vnpy.trader.utility import extract_vt_symbol
from vnpy.trader.setting import SETTINGS
from vnpy_tqsdk.tqsdk_datafeed import TqsdkDatafeed

datafeed: TqsdkDatafeed = get_datafeed()
database = get_database()
cur_path = Path(__file__).parent

# df = datafeed.query_all(ind_class="CONT", interval=Interval.HOUR, data_length=1e4)
# df.to_parquet(cur_path / "cont_df.parquet", index=False)
df = (
    pl.read_parquet(cur_path / "cont_df.parquet")
    .with_columns(pl.col("datetime").cast(pl.Datetime(time_unit="ns", time_zone=DB_TZ)))
    .rename({"datetime": "open_time", "symbol": "jj_code"})
    .with_columns(
        close_time=pl.col("open_time")
        + pl.duration(minutes=59, seconds=59, milliseconds=999)
    )
)

pass
