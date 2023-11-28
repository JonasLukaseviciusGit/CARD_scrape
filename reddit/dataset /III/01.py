import json

path = r"C:\Users\HP\Desktop\redditscrape\final\PostFoldersContainer\001_0.json"

with open(path, 'r') as f:
    data = json.load(f)

submission = data['submission']
comments = data['comments']
comment = comments[0]

keys = comment.keys()
for key in keys:
    print(key)
    print(comment[key])
    print('')

new_submission = {
    'title': submission['title'],
    'author': submission['author'],
    'created_utc': submission['created_utc'],
    'text': submission['selftext'],
    'ups': submission['ups'],
    'downs': submission['downs'],
    'score': submission['score'],
    'num_comments': submission['num_comments'],
    'id': submission['id'],
    'other_data': {
        'over_18': submission['over_18'],
        'thumbnail': submission['thumbnail'],
        'url': submission['url'],
        'link_flair_text': submission['link_flair_text'],
        'edited': submission['edited'],
        'selftext': submission['selftext'],
        'selftext_html': submission['selftext_html'],
        'user_reports': submission['user_reports'],
        'author_flair_text': submission['author_flair_text'],
        'distinguished': submission['distinguished'],
        'domain': submission['domain'],
        'subreddit_id': submission['subreddit_id'],
        'subreddit': submission['subreddit'],
        'report_reasons': submission['report_reasons'],
        'is_self': submission['is_self'],
        'permalink': submission['permalink'],
        'stickied': submission['stickied'],
        'gilded': submission['gilded'],
        'secure_media': submission['secure_media'],
        'media': submission['media'],
        'mod_reports': submission['mod_reports'],
        'secure_media_embed': submission['secure_media_embed'],
        'author_flair_css_class': submission['author_flair_css_class'],
        'media_embed': submission['media_embed'],
        'banned_by': submission['banned_by'],
        'retrieved_on': submission['retrieved_on']
    }
}

new_comment = {
    'author': comment['author'],
    'ups': comment['ups'],
    'downs': comment['downs'],
    'created_utc': comment['created_utc'],
    'body': comment['body'],
    'score': comment['score'],
    'other_data': {
        'distinguished': comment['distinguished'],
        'controversiality': comment['controversiality'],
        'parent_id': comment['parent_id'],
        'gilded': comment['gilded'],
        'score_hidden': comment['score_hidden'],
        'subreddit': comment['subreddit'],
        'id': comment['id'],
        'name': comment['name'],
        'subreddit_id': comment['subreddit_id'],
        'archived': comment['archived'],
        'edited': comment['edited'],
        'retrieved_on': comment['retrieved_on'],
        'link_id': comment['link_id'],
        'author_flair_text': comment['author_flair_text'],
        'author_flai_css_class': comment['author_flair_css_class']
    }
}
