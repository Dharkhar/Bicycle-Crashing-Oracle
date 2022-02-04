class Member:
    def __init__(
        self, name: str, linkedin_url: str = None, github_url: str = None
    ) -> None:
        self.name = name
        self.linkedin_url = linkedin_url
        self.github_url = github_url

    def sidebar_markdown(self):

        markdown = f'<b style="display: inline-block; vertical-align: middle; height: 100%">{self.name}</b>'

        if self.linkedin_url is not None:
            markdown += f' <a href={self.linkedin_url} target="_blank"><img src="https://pnggrid.com/wp-content/uploads/2021/05/linkedin-logo-white-1024x1024.png" alt="linkedin" width="20" style="vertical-align: middle; margin-left:20px"/></a> '

        if self.github_url is not None:
            markdown += f' <a href={self.github_url} target="_blank"><img src="https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg" alt="github" width="25" style="vertical-align: middle; margin-left: 5px"/></a> '

        return markdown
