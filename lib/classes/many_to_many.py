class Article:
    # Initializing all to empty array
    all = list()

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if hasattr(self, 'title'):
             AttributeError('Title cannot be changed')
        # The below checks if the new title is a string and is between 5 and 50 characters
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
             ValueError('Title must be a string between 5 and 50 characters')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine
    
    # setter method allows assigning a new value to magazine attribute.
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")

class Author:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    # setter method allows assigning a new value to name attribute.
    @name.setter
    def name (self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            # Checks if name is a string
            if isinstance(new_name, str):
                # Checks the length of the new_name
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")

    def articles(self):
        # returns a list of articles written by the author.
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        # Returns the list of magazines the Author has made contributions
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # Adds an article to the magazine
        return Article(self, magazine, title)

    def topic_areas(self):
        # Returns a list of topic areas for all articles by author.(which he has contributed to)
        areas = list({magazine.category for magazine in self.magazines()})
        return areas if areas else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    # setter method for assigning a new value to name attribute.
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
             ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    # setter method for assigning a new value to category attribute.
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
             ValueError("Category must be a non-empty string")

    # articles methodreturns a list of articles in the magazine.
    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})
    
    def article_titles(self):
        article_titles = [article.title for article in self.articles()]
        return article_titles if article_titles else None

    # contributing_authors returns a list of authors who have contributed multiple articles to the magazine.
    # First counting the number of articles contributted by each Author and filters out those contributing more than two articles.
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count >= 2] or None