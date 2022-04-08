# lotr
FastAPI based on the epic Lord of the Rings

### Fetching data from source API
At the moment, the first step is to fetch all data from the source api by making a request to `/fetch_data` endpoint,
effectively calling the `fetch_data_from_source_api()` function.

In the future, this data will be polled routinely via a cronjob.

### TODO
- [.] Make database models
- [ ] Deserialize fetched data as a model
- [ ] Save fetched data into db
- [ ] Expose data on my own API
- [ ] Do something cool with data like create random dialogue from quotes between given characters
