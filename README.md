# Telegram Group Message Download

Download all messages from a group to a csv file. Utility to get group ids as well.

## Get ids
```
poetry run python chatids.py
```
## Download messages from group

```
poetry run python download.py --group ### --path ./output.csv
```

### TODO

- Expose parameter limit for chat ids count