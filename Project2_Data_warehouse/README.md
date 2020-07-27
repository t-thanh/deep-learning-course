# Project 2: Data Warehouse
## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

Data engineer are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. Database must be tested and ETL pipeline by running queries given by the analytics team from Sparkify and compare results with their expected results.

## Project description
Applying knowledges of data warehouses and AWS to build ETL pipeline for database hosted on Redshift
- load data from S3 to staging tables on Redshift 
- execute SQL statements that create the analytics tables from these staging tables

## Project Datasets
There are two datasets that reside in S3. Here are the S3 links to each:
- Song data: `s3://udacity-dend/song_data`
- Log data: `s3://udacity-dend/log_data`
Log data json path: `s3://udacity-dend/log_json_path.json`

## Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.
```python
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```
And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like
```python
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

## Log Dataset 
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```python
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```

## Instruction
- Step 1: fill in the AWS `key`, `secret`, and the defined server `region` in `dwh.cfg`
- Step 2: execute `python create_dwh.py` to create the cluster 
- Step 3: run `python create_tables.py` to create the tables, including staging as well as fact and dimension tables
- Step 4: execute `python etl.py` to run the ETL pipeline
- Step 5: don't forget to `python delete_dwh.py` to delete the cluster to avoid charging cost after testing