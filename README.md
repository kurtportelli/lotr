# lotr
FastAPI based on the epic Lord of the Rings

### Fetching data from source API
At the moment, the first step is to fetch all data from the source api by making a request to `/fetch_data` endpoint,
effectively calling the `fetch_data_from_source_api()` function.

In the future, this data will be polled routinely via a cronjob.