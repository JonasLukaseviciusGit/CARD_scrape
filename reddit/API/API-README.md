# API-README
Retrieving Reddit data via API (praw)

---
### get_last_submission_ids
Returns a list of ids regarding a specified number of the latest submissions.

### get_comment_ids_by_submission_id
Returns a list of ids regarding comments to a particular submission.

### parse_submission
Parses useful data regarding submission:<br>

url<br>
user<br>
details_about_user: username, karma, user_created_at<br>
posted_at<br>
header<br>
votes<br>
text<br>

Also comments and comments to those comments (and so on):<br>
comment_id<br>
user<br>
commented_at<br>
votes<br>
text<br>
replies<br>
