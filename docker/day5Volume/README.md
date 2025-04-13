We’ll modify yesterday’s setup so that our app:

Saves the counter to a local file

Uses a volume to persist that data even if the container stops or is rebuilt

This creates a named volume (counter_data) that maps to /data in the container, which the app uses to store the counter file.


OUTPUT :


Visit: http://localhost:5000

💡 Refresh the page → count increases
💥 Stop the container and rerun → counter is not lost
