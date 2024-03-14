# Learning Records

## Development
### Scheduling Jobs
Python 中定時任務的解決方案有四種：crontab、 scheduler、 Celery、 APScheduler，其中 crontab 不適用於多服務器配置、scheduler 功能過於簡單、 Celery 依賴套件多，較耗資源。最建議的解決方案是 APScheduler。
- `crontab`
- `scheduler`
- `Celery`
- [`APScheduler`](/dev/apscheduler)
    - 提供了基於日期、固定時間間隔以及 crontab 類型的任務
    - 可在程序運行過程中動態的新增任務和刪除任務
    - 在任務運行過程中，可把任務存儲起來，下次啟動運行依然保留之前的狀態
    - 支援跨平台運行

### API Development
- `FastAPI`
    - [API simplest template](/dev/fastapi)

### Online Coding IDE
- `Colab`
    - [Colab Tricks: Prevent from disconnect](/dev/colab/Colab-Tricks-Prevent-from-disconnect.md)

## Marketing

### Facebook Ads
- [Interest search script](/marketing/fb/190902_fbmktapi_interestSearchScript.py)
