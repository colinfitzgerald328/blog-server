import frontmatter

def parse_metadata(markdown_content):
    # Parse the front matter and content from the markdown
    post = frontmatter.loads(markdown_content)
    # Extract the metadata from the parsed front matter
    metadata = post.metadata
    # Extract the markdown content from the parsed markdown
    markdown_content = post.content
    return metadata, markdown_content
