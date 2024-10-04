# news_sources.py

news_sources = [
    {
        'name': 'BBC',
        'url': 'https://www.bbc.com/news',
        'find_all_args': {'attrs': {'data-testid': 'card-headline'}}
    },
    {
        'name': 'CNN',
        'url': 'https://edition.cnn.com',
        'find_all_args': {'name': 'span', 'class_': 'container__headline-text'}
    },
    {
        'name': 'Reuters',
        'url': 'https://www.reuters.com/',
        'find_all_args': {'class_': 'Headline'}  # Update this class based on the actual HTML structure
    }
]