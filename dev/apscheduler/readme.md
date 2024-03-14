### 四個基本組件：

1. 觸發器（triggers）：觸發器就是根據指定的觸發方式，比如是按照時間間隔，還是按照 crontab觸發，觸發條件是什麽等。每個任務都有自己的觸發器。

2. 任務存儲器（job stores）：任務存儲器是可以存儲任務的地方，默認情況下任務保存在內存，也可將任務保存在各種數據庫中。任務存儲進去後，會進行序列化，然後也可以反序列化提取出來，繼續執行。

3. 執行器（executors）：執行器的目的是安排任務到線程池或者進程池中運行的。

4. 調度器（schedulers）：任務調度器是屬於整個調度的總指揮官。他會合理安排作業存儲器、執行器、觸發器進行工作，並進行添加和刪除任務等。調度器通常是只有一個的。開發人員很少直接操作觸發器、存儲器、執行器等。因為這些都由調度器自動來實現了。


### triggers
triggers 有兩種，第一種是 interval，第二種是 crontab。
interval可以具體指定多少時間間隔執行一次。crontab可以指定執行的日期策略。

1. date triggers: 在某個日期時間只觸發一次事件。
2. interval triggers: 
在固定的時間間隔觸發事件。
interval的觸發器可以設置以下的觸發參數：

- weeks：周。(`int`)
- days：一個月中的第幾天。(`int`)
- hours：小時。(`int`)
- minutes：分鐘。(`int`)
- seconds：秒。(`int`)
- start_date：間隔觸發的起始時間。
- end_date：間隔觸發的結束時間。
- jitter：觸發的時間誤差。

3. crontab triggers:
在某個確切的時間周期性的觸發事件。
可以使用的參數如下：
- year：4位數字的年份。
- month：1-12月份。
- day：1-31日。
- week：1-53周。
- day_of_week：一個禮拜中的第幾天（ 0-6或者 mon、 tue、 wed、 thu、 fri、 sat、 sun）。
- hour： 0-23小時。
- minute： 0-59分鐘。
- second： 0-59秒。
- start_date： datetime類型或者字符串類型，起始時間。
- end_date： datetime類型或者字符串類型，結束時間。
- timezone：時區。
- jitter：任務觸發的誤差時間。

### 調度器 Scheduler
- BlockingScheduler：適用於調度程序是進程中唯一運行的進程，調用 start 函數會阻塞當前線程，不能立即返回。
- BackgroundScheduler：適用於調度程序在應用程序的後臺運行，調用 start 後主線程不會阻塞。
- AsyncIOScheduler：適用於使用了 asyncio模塊的應用程序。
- GeventScheduler：適用於使用 gevent模塊的應用程序。
- TwistedScheduler：適用於構建 Twisted的應用程序。
- QtScheduler：適用於構建 Qt的應用程序。

### 任務存儲器 JobStore
任務存儲器的選擇有兩種。一是內存，也是默認的配置。二是數據庫。
使用內存的方式是簡單高效，但不好的是，一旦程序出現問題，重新運行的話，會把之前已經執行了的任務重新執行一遍。
數據庫則可以在程序崩潰後，重新運行可以從之前中斷的地方恢復正常運行。
有以下幾種選擇：
- MemoryJobStore：沒有序列化，任務存儲在內存中，增刪改查都是在內存中完成。
- SQLAlchemyJobStore：使用 SQLAlchemy這個 ORM框架作為存儲方式。
- MongoDBJobStore：使用 mongodb作為存儲器。
- RedisJobStore：使用 redis作為存儲器。

### 執行器 Executor
執行器的選擇取決於應用場景。通常默認的 ThreadPoolExecutor已經在大部分情況下是可以滿足我們需求的。如果我們的任務涉及到一些 CPU密集計算的操作。那麽應該考慮 ProcessPoolExecutor。然後針對每種程序， apscheduler也設置了不同的 executor：

- ThreadPoolExecutor：線程池執行器。
- ProcessPoolExecutor：進程池執行器。
- GeventExecutor： Gevent程序執行器。
- TornadoExecutor： Tornado程序執行器。
- TwistedExecutor： Twisted程序執行器。
- AsyncIOExecutor： asyncio程序執行器。

#### 參考資料
- https://zhuanlan.zhihu.com/p/144506204