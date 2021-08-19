# Synchronization and Reporting Architecture  (SARA)

SARA is designed to help centralize reporting, synchronization and other functions.

## Development

```shell
poetry install
```

### Migrations

Make modifications to the entities, and then run the following:

`poetry run sara db revision --autogenerate -m "General description of what is happening""`
