from datetime import datetime, timedelta

class StringTime:
    """
    時間を時、分、秒、マイクロ秒で保持

    時刻表記
        (区切り文字):; ：；　

        case1
            00:00
        case2
            0000 -> 00:00
        case3
            000 -> 0:00

    浮動小数点表記
        (区切り文字),.，．

        1.5 -> 1:30


    加算
    減算
    datetimeに変換
    datetimeから変換

    要件に合わない入力をしたときは無視されます

    """

    def __init__(self,str_time=None):
        self.__SEPARATORS = tuple(":; ：；　")
        self.__DECIMAL_POINTS = tuple(",.，．")
        self._time = "0:00"
        self._hour = 0
        self._minute = 0
        self._second = 0
        self._microsecond = 0
        if str_time:
            self.time = str_time

    def __str__(self):
        return self.time

    @property
    def time(self):
        return f"{self.hour}:{self.minute}"

    @property
    def hour(self):
        return str(self._hour).zfill(2)

    @property
    def minute(self):
        return str(self._minute).zfill(2)

    @property
    def second(self):
        return str(self._second).zfill(2)

    @property
    def microsecond(self):
        return str(self._microsecond)

    @property
    def float_time(self):
        """
            参照用
            計算処理には使わないほうがいいよ
        """
        return int(self.hour) + int(self.minute)/60 + int(self.second)/60/60 + int(self.microsecond)/60/60/(10^6)

    @property
    def serial_time(self):
        """
            HH:MM形式の時間表記をexcelのシリアル時間に変換します。
            また、0:00の時はブランクにします。
        """
        if any(map(int,(self.hour,self.minute))):
            return int(self.hour) / 24 + int(self.minute) / 24 / 60
        else:
            return ""

    @time.setter
    def time(self,str_time,long=False):

        # int,floatの場合strに変換
        if type(str_time) in (int,float):
            str_time = str(str_time)

        if type(str_time) is str:
            symbol = self._check_symbol(str_time)

            # 区切り文字が1種類の場合
            if symbol:
                items = str_time.split(symbol)

                if all([self._isnum(i) for i in items]): # すべて数値の場合
                    # 時刻表記の場合
                    if symbol in self.__SEPARATORS and self._check_time_items(items):
                        self._set_clock_time(items)

                    # 浮動小数点表記の場合
                    elif symbol in self.__DECIMAL_POINTS and len(items) <= 2:
                        self._set_decimal_time(items)

            # 区切り文字がない場合
            elif symbol is None:
                if long or len(str_time) <= 2:
                    self.hour = str_time
                else:
                    self.hour = str_time[:-2]
                    self.minute = str_time[-2:]

            else:
                print("error!")

        # 入力がdatetime型の場合
        elif type(str_time) is datetime:
            now = datetime(
                year = datetime.now().year,
                month = datetime.now().month,
                day = datetime.now().day,
                hour = str_time.hour,
                minute = str_time.minute,
                second = str_time.second,
                microsecond = str_time.microsecond
            )
            diff = str_time - now
            self.hour = int(str_time.hour) + int(diff.total_seconds() / 3600)
            self.minute = str_time.minute
            self.second = str_time.second
            self.microsecond = str_time.microsecond

    @hour.setter
    def hour(self,num):
        if self._isnum(num):
            self._hour = int(num)

    @minute.setter
    def minute(self,num):
        if self._isnum(num):
            self._minute = int(num)%60
            self._hour += int(num)//60

    @second.setter
    def second(self,num):
        if self._isnum(num):
            self._second = int(num)%60
            self._minute += int(num)//60

    @microsecond.setter
    def microsecond(self,num):
        if self._isnum(num):
            self._microsecond = int(num)%(10**6)
            self._second += int(num)//(10**6)

    def _check_symbol(self,str_time):
        """
            使用している記号が1種類のときはその記号を返す
            記号を使用していないときはNoneを返す
            複数混在している場合はFalseを返す
        """
        symbol_count = list({i for i in str_time if i in self.__SEPARATORS or i in self.__DECIMAL_POINTS})

        if len(symbol_count) == 1:
            return symbol_count[0]
        elif len(symbol_count) == 0:
            return None
        else:
            return False

    def _check_time_items(self,items):
        """
            時刻表記の場合に区切り文字で分割した数が4以下かつ
            分割した要素に長さ0のものが含まれなければTrueを返す
        """
        item_count = [len(i) for i in items]
        if len(item_count) <= 4 and min(item_count) > 0:
            return True
        else:
            return False

    def _set_clock_time(self,items):
        """
            時刻をセット
        """
        if len(items) == 1:
            items.append(0)
        if len(items) == 2:
            items.append(0)
        if len(items) == 3:
            items.append(0)

        self.hour = items[0]
        self.minute = items[1]
        self.second = items[2]
        self.microsecond = items[3]

    def _set_decimal_time(self,items):
        """
            小数点入力したときの時刻セット
        """
        #小数点以下の時間をマイクロ秒に直す
        tmp_microseconds = float(f"0.{items[1]}")*60*60*10**6
        tmp_seconds = tmp_microseconds // (10**6)
        tmp_minutes = tmp_seconds // 60
        tmp_microseconds %= 10**6
        tmp_seconds %= 60

        self.hour = items[0]
        self.minute = tmp_minutes
        self.second = tmp_seconds
        self.microsecond = tmp_microseconds

    def _isnum(self,num):
        try:
            int(num)
        except:
            return False
        return True

    def __add__(self,obj):
        if type(obj) is StringTime:
            ret_obj = StringTime()

            ret_obj.hour = int(self.hour) + int(obj.hour)
            ret_obj.minute = int(self.minute) + int(obj.minute)
            ret_obj.second = int(self.second) + int(obj.second)
            ret_obj.microsecond = int(self.microsecond) + int(obj.microsecond)

            return ret_obj

    def __sub__(self,obj):
        if type(obj) is StringTime:
            ret_obj = StringTime()

            ret_obj.hour = int(self.hour) - int(obj.hour)
            ret_obj.minute = int(self.minute) - int(obj.minute)
            ret_obj.second = int(self.second) - int(obj.second)
            ret_obj.microsecond = int(self.microsecond) - int(obj.microsecond)

            return ret_obj

    @classmethod
    def total_time(self,time_arr):
        ret_obj = StringTime()
        for time in time_arr:
            ret_obj += StringTime(time)
        return ret_obj

    def to_datetime(self):
        today = datetime.today()
        ret_datetime = datetime(
            year = today.year,
            month = today.month,
            day = today.day,
            hour = int(self.hour) % 24,
            minute = int(self.minute),
            second = int(self.second),
            microsecond = int(self.microsecond),
        ) + timedelta(days=int(self.hour) // 24)
        return ret_datetime


