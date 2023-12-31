# API-README
Retrieving Reddit data via API (praw)

---
### get_last_submission_ids
Returns a list of ids regarding a specified number of the latest submissions.

### get_comment_ids_by_submission_id
Returns a list of ids regarding comments to a particular submission.

### parse_submission
Parses useful data regarding submission:<br>

* url
* user
* user_details: username, karma, created_at
* posted_at
* header
* votes
* text
* comments

Also comments and comments to those comments (and so on):<br>

* comment_id
* user
* commented_at
* votes
* text
* replies

### parse_multiple_last_submissions
Uses process similar to parse_submission. Does the following:
1. Gets the last 10 submission ids (this number can be changed).
2. Creates a folder.
3. Parses every id and saves resulting dictionary in the folder naming it according to its id.
