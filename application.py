import os
from flask import Flask, url_for
from utilities import parse_metadata


# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/', methods=['GET'])
def server_status():
    return {"operation": "success",
            "server_status": "operational"
            }


@application.route('/blog/posts/')
def list_posts():
    posts = []
    for filename in os.listdir('posts'):
        if filename.endswith('.md'):
            with open(os.path.join('posts', filename), 'r') as file:
                content = file.read()
            # Extract metadata (such as title and date) from the markdown file
            # You can use a library like frontmatter or YAML to parse metadata
            # and store it in a dictionary
            metadata, md_content = parse_metadata(content)
            post = {
                'title': metadata['title'],
                'date': metadata['date'],
                'url': url_for('list_posts') + filename[:-3],
                'excerpt': md_content[:100] + '...',
            }
            posts.append(post)
    # Render a template that lists all the blog posts
    return posts


# run the app.
if __name__ == "__main__":
    application.run(debug=True)