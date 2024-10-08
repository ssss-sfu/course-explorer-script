# course-explorer-script

## Description

Script to generates all the course requirements from [SFU Course Outlines REST API](http://www.sfu.ca/outlines/help/api.html). Used specifically to get all course requirements for Software Systems Degree requirements (Fall 2023).

The JSON data will be used by [sfussss.org](https://www.sfussss.org/) for its course explorer feature.

## Installation

1. Install python3
2. Run `python3 main.py`
3. See it generates `courses.json` in `result` directory

Latest generated `courses.json` can be viewed at https://github.com/ssss-sfu/ssss-sfu.github.io/blob/master/public/jsons/courses.json

JSON GET API ENDPOINT at https://raw.githubusercontent.com/ssss-sfu/course-explorer-script/main/result/courses.json
