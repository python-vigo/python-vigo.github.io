#!/usr/bin/env python
import datetime
import json
from pathlib import Path

from conf import BASE_URL


base_dir = Path()


def generate_events_file():
    # Get last meeting post
    posts_dir = Path('posts')
    last_post = sorted(posts_dir.glob('reunion_del_grupo_*'))[-1]

    # Get post metadata
    post_metadata = {}

    with last_post.open('r') as post_file:
        for line in post_file:
            if not line.startswith('.. '):
                break
            # Post metadata structure is like:
            # .. date: 2018-11-05 11:09:30 UTC+02:00
            key, value = (x.strip() for x in line[3:].split(':', 1))
            post_metadata.update({key: value})

    # We need the date of the meeting, not the day of publication so we
    # extract it from the slug
    meeting_ymd = post_metadata['slug'][-8:]
    meeting_date = datetime.datetime.strptime(meeting_ymd, '%Y%m%d')
    meeting_timestamp = int(meeting_date.timestamp() * 1000)

    events_data = {
        "date": meeting_timestamp,
        "title": post_metadata['title'],
        "url": BASE_URL + 'posts/' + post_metadata['slug'] + '/'
    }

    # Write events.json file
    events_file = base_dir.joinpath('files/events.json')
    with events_file.open('w') as ef:
        json.dump(events_data, ef, indent=4)


# Call custom deployment methods
generate_events_file()

