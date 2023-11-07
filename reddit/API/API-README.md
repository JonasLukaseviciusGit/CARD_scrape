# API-README
Retrieving Reddit data via API (praw)

---
### get_last_submission_ids
Returns a list of ids regarding a specified number of the latest submissions.

### get_comment_ids_by_submission_id
Returns a list of ids regarding comments to a particular submission.

### parse_submission
Parses useful data regarding submission:

url
user
details_about_user: username, karma, user_created_at
posted_at
header
votes
text

Also comments and comments to those comments (and so on):
comment_id
user
commented_at
votes
text
replies
