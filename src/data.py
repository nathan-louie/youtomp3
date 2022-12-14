import re


class Data:
    def __init__(self):
        self.user = ""
        self.path = ""
        self.youtube_links = []

    def __str__(self):
        return f"User: {self.user} | Path: {self.path} | Youtube Links: {self.youtube_links}"

    def _parse_user(self, path):
        return (lambda x: x)(
            *re.findall(r"(?:Users/)(\w+).*", path))

    def _parse_path(self):
        return f"~/Downloads/%(title)s.%(ext)s"

    def add_path(self, data_path: str):
        self.user = self._parse_user(data_path)
        self.path = self._parse_path()

    def add_youtube_links(self, youtube_link: str):
        if "/results?search_query=" not in youtube_link:
            self.youtube_links.append(youtube_link.split("&")[0])

    def has_data(self):
        return True if self.user != "" and self.path != "" and self.youtube_links is not [] else False
